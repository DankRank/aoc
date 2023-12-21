#!/usr/bin/env python3
import sys
import functools
target = 26501365
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
m = [line.rstrip() for line in sys.stdin] 
rocks = {(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == '#'}
start = [(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'S'][0]
w, h = len(m[0]), len(m)
assert sum(start)%2 == 0
assert w%2 == 1
assert w == h
# this one relies on a lot of assumptions that don't hold for the example
assert target%w == w//2 # like this crazy one!
# or the fact that the input has lateral roads going through the start point
# or the wide diagonal roads
# the last two facts guarantee that the area will grow evenly
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

known_chunks = [set(), set()]
prev_chunks, next_chunks = {}, {(0, 0): frozenset({start})}
generation = 0
sols = [1]
def update(i, j, ns):
    if len(ns) and (i, j) not in known_chunks[(i+j)%2]:
        if (i, j) not in next_chunks:
            next_chunks[i, j] = ns
        else:
            next_chunks[i, j] |= ns
while generation != w//2 + 2*w:
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
            known_chunks[(i+j)%2].add((i, j))
    sols.append(sum(len(v) for v in next_chunks.values())+sum(maxes[i][generation%2]*len(known_chunks[i]) for i in range(2)))

f0 = sols[w//2]
f1 = sols[w//2 + w]
f2 = sols[w//2 + 2*w]
# f0 = c
# f1 = a + b + c
# f2 = 4a + 2b + c
c = f0
a = (f2 - 2*f1 + c)//2
b = f1 - a - c
q = lambda x: a*x*x + b*x + c
assert f0 == q(0)
assert f1 == q(1)
assert f2 == q(2)
print(q(target//w))
