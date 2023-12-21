#!/usr/bin/env python3
import sys
import functools
targets = [26501365] if len(sys.argv) < 2 else [int(s) for s in sys.argv[1:]]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
m = [line.rstrip() for line in sys.stdin] 
rocks = {(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == '#'}
start = [(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'S'][0]
w, h = len(m[0]), len(m)
assert sum(start)%2 == 0
assert w%2 == 1
assert w == h
# Not doing a check here, but the ring around each chunks gives us a few important invariants including:
# - once you enter a chunk, it will always be completely filled eventually
# - once you enter a chunk, it will never be empty again
# - start chunk is also completely filled (unless you never leave the starting chunk)
# by "completely filled" i mean one of the four patterns found by the findmaxes function
def neighbors(s):
    if s[0] > 0   and (s[0]-1, s[1]) not in rocks:
        yield 0, (s[0]-1, s[1])
    if s[0] < w-1 and (s[0]+1, s[1]) not in rocks:
        yield 0, (s[0]+1, s[1])
    if s[1] > 0   and (s[0], s[1]-1) not in rocks:
        yield 0, (s[0], s[1]-1)
    if s[1] < h-1 and (s[0], s[1]+1) not in rocks:
        yield 0, (s[0], s[1]+1)
    if s[0] == 0:
        yield 3, (w-1, s[1])
    if s[0] == w-1:
        yield 1, (0, s[1])
    if s[1] == 0:
        yield 2, (s[0], h-1)
    if s[1] == h-1:
        yield 4, (s[0], 0)

@functools.cache
def bfs_step(prev_states):
    next_states = [set(), set(), set(), set(), set()]
    for s in prev_states:
        for d, ns in neighbors(s):
            next_states[d].add(ns)
    return tuple(frozenset(x) for x in next_states)

# find the maximum amount in one chunk
# we have to use bfs for this because of inaccessible cells
def findmaxes(x, y):
    maxeven = None
    maxodd  = None
    states = frozenset({(x, y)})
    even = 1
    while even != maxeven:
        maxeven = even
        states = bfs_step(states)[0]
        maxodd = len(states)
        states = bfs_step(states)[0]
        even = len(states)
    return maxeven, maxodd
maxes = [findmaxes(0, 0), findmaxes(1, 0)]

# Step 1: run the naive BFS for 500 steps and record all possible states
# this is the slowest part
known_chunks = set()
prev_chunks, next_chunks = {}, {(0, 0): frozenset({start})}
generation = 0
def update(i, j, ns):
    if len(ns) and (i, j) not in known_chunks:
        if (i, j) not in next_chunks:
            next_chunks[i, j] = ns
        else:
            next_chunks[i, j] |= ns
mstates = {}
mstates[next_chunks[0, 0]] = 0
mnext = {}
mbirth = {}
#mtrack = {}
#mtrackheads = {}
while generation != 500:
    for i, j in prev_chunks.keys() | next_chunks.keys():
        pv = prev_chunks[i, j] if (i, j) in prev_chunks else None
        nv = next_chunks[i, j] if (i, j) in next_chunks else None
        if nv is not None and nv not in mstates:
            mstates[nv] = len(mstates)
        pv = mstates[pv] if pv in mstates else -1
        nv = mstates[nv] if nv in mstates else -2
        if pv == -1:
            count = 0
            #if nv not in mtrackheads:
            #    mtrack[nv] = mtrackheads[nv] = len(mtrackheads)
            for d, di in enumerate(dirs):
                if (i+di[0], j+di[1]) in prev_chunks:
                    count += 1
            assert count < 3
            for d, di in enumerate(dirs):
                if (i+di[0], j+di[1]) in prev_chunks:
                    p = mstates[prev_chunks[i+di[0], j+di[1]]]
                    if p not in mbirth:
                        mbirth[p] = [None]*4
                    if mbirth[p][d^2] is None:
                        mbirth[p][d^2] = (nv, 3-count)
                    assert mbirth[p][d^2] == (nv, 3-count)
        if pv != -1:
            if pv not in mnext:
                mnext[pv] = nv
                #if nv != -2:
                #    if nv not in mtrack:
                #        mtrack[nv] = mtrack[pv]
                #    assert mtrack[nv] == mtrack[pv]
            assert mnext[pv] == nv
    # make sure number of unique states per step doesn't explode
    assert len(set(mstates[nv] for nv in next_chunks.values())) <= 16
    prev_chunks, next_chunks = next_chunks, {} 
    generation += 1
    for i, j in prev_chunks:
        a, b, c, d, e = bfs_step(prev_chunks[i, j])
        update(i, j, a)
        update(i+1, j, b)
        update(i, j-1, c)
        update(i-1, j, d)
        update(i, j+1, e)
        if len(next_chunks[i, j]) == maxes[(i+j)%2][generation%2]:
            del next_chunks[i, j]
            known_chunks.add((i, j))
    #s = ''
    #for j in range(-25, 26):
    #    for i in range(-25, 26):
    #        s += '#' if (i, j) in known_chunks else '?' if (i, j) in prev_chunks else 'n' if (i, j) in next_chunks else '.'
    #    s += '\n'
    #if 'n' in s:
    #    print(s)
    #    print(generation, len(mstates), bfs_step.cache_info())
mnext[-2] = -2

# Step 2: count the number of each state after 26501365 iterations

def freezemap(m):
    return frozenset((k, frozenset(v.items())) for k, v in m.items())

# takes frozenset of keys returns frozenset of pairs
@functools.cache
def mstep(states):
    potentialbirths = set()
    newstates = {}
    def add(nst, st):
        if nst not in newstates:
            newstates[nst] = {}
        if st not in newstates[nst]:
            newstates[nst][st] = 0
        newstates[nst][st] += 1
    for st in states:
        if st[0] in mbirth:
            for d, birth in enumerate(mbirth[st[0]]):
                if birth is not None:
                    nst = (birth[0], st[1]^1)
                    if birth[1] == 1:
                        if nst not in potentialbirths:
                            potentialbirths.add(nst)
                        else:
                            potentialbirths.remove(nst)
                            add(nst, st)
                    else:
                        add(nst, st)
    assert len(potentialbirths) == 0
    for st in states:
        nst = (mnext[st[0]], st[1])
        add(nst, st)
    return freezemap(newstates)

# takes (frozenset of pairs, dict) returns dict
def applystep(newres, oldres):
    res = {}
    for i, j in newres:
        poly = {}
        for k, l in j:
            for m, n in oldres[k].items():
                if m not in poly:
                    poly[m] = 0
                poly[m] += n*l
        res[i] = poly
    return res

# takes dict, returns frozenset of keys
def extractkeys(res):
    return frozenset(res.keys())

# recursive memoization!
def stepdoubler(stepfunc):
    @functools.cache
    def f(states):
        res1 = stepfunc(states)
        res = {k: dict(v) for k, v in res1}
        res2 = stepfunc(extractkeys(res))
        return freezemap(applystep(res2, res))
    return f

ggstep = [mstep]
for i in range(1, 16):
    ggstep.append(stepdoubler(ggstep[-1]))

def solve(target):
    left = target
    res = {(0, 0): {-1: 1}}
    for i in range(len(ggstep)-1, -1, -1):
        while left > 1<<i:
            #print(left)
            left -= 1<<i
            res = applystep(ggstep[i](extractkeys(res)), res)
    return res

# Step 3: recover the results
mcounts = {v: len(k) for k, v in mstates.items()}
def getsolution(res):
    count = 0
    for k, v in res.items():
        print(k)
        state, parity = k
        if state == -2:
            count += v[-1] * maxes[parity][target%2]
        else:
            count += v[-1] * mcounts[state]
    return res

print(' '.join(str(getsolution(solve(target))) for target in targets))
