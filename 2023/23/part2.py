#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def neighbors(s):
    if s[1] == 0:
        yield (s[0], s[1]+1)
    elif s[1] == len(m)-1:
        yield (s[0], s[1]-1)
    else:
        for i in range(4):
            ns = (s[0]+dirs[i][0], s[1]+dirs[i][1])
            if m[ns[1]][ns[0]] != '#':
                yield ns

# calculate distances between each intersection
# not very optimized (calculates a->b and b->a separately)
endpoints = [(1, 0), (len(m[0])-2, len(m)-1)]
def follow(s, i):
    count = 1
    last = s
    s = list(neighbors(s))[i]
    while True:
        if s in endpoints:
            break
        nls = list(neighbors(s))
        if len(nls) > 2:
            break
        last, s = s, nls[1] if nls[0] == last else nls[0]
        count += 1
    return s, count
adj = {}
tocheck = {(1, 0)}
while len(tocheck):
    s = tocheck.pop()
    adj[s] = {}
    for i in range(len(list(neighbors(s)))):
        ns, count = follow(s, i)
        assert ns not in adj[s] # surprisingly, this is true
        adj[s][ns] = count
        if ns not in adj:
            tocheck.add(ns)

#known = set()
#print('graph {')
#for i in adj:
#    print(f'"{i}"')
#for i in adj:
#    for j in adj[i]:
#        if (j, i) not in known:
#            known.add((i, j))
#            print(f'"{i}" -- "{j}" [label="{adj[i][j]}"]')
#print('}')
#sys.exit(0)

start, target = (1, 0), (len(m[0])-2, len(m)-1)

relabel = {start: 0, target: 1}
start, target = 0, 1
for i in adj:
    if i not in relabel:
        relabel[i] = len(relabel)
adj = {relabel[i]: {relabel[j]: k for j, k in v.items()} for i, v in adj.items()}

maxdist = 0
prev_states, next_states = set(), {(start, 0, 0)}
while len(next_states):
    prev_states, next_states = next_states, set()
    for s, dist, history in prev_states:
        history |= 1<<s
        for ns, ndist in adj[s].items():
            if 1<<ns & history == 0:
                ndist += dist
                if ns == target:
                    if ndist > maxdist:
                        maxdist = ndist
                else:
                    next_states.add((ns, ndist, history))
print(maxdist)
