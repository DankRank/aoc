#!/usr/bin/env python3
import sys
import queue
m = [line.rstrip() for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch == 'E':
            target = (x, y)
        elif ch == 'S':
            start = (x, y)

def neighbors(s):
    nx = s[0] + dirs[s[2]][0]
    ny = s[1] + dirs[s[2]][1]
    if m[ny][nx] != '#':
        yield (nx, ny, s[2]), 1
    yield (s[0], s[1], (s[2]+1)%4), 1000
    yield (s[0], s[1], (s[2]+3)%4), 1000

minp = float('inf')
dist = {(*start, 0): 0}
prev = {}
visited = set()
q = queue.PriorityQueue()
q.put((0, (*start, 0)))
while not q.empty():
    s = q.get()[1]
    if s in visited:
        continue
    for ns, ndist in neighbors(s):
        if ns not in visited:
            ndist += dist[s]
            if ns not in dist or ndist < dist[ns]:
                prev[ns] = {s}
                dist[ns] = ndist
                if ns[:2] == target and ndist < minp:
                    minp = ndist
                elif ndist < minp:
                    q.put((ndist, ns))
            elif ns in dist and ndist == dist[ns]:
                prev[ns].add(s)
    visited.add(s)
print(minp)

spots = set()
next_states = set()
for i in range(4):
    s = (*target, i)
    if s in dist and dist[s] == minp:
        next_states.add(s)

while len(next_states):
    prev_states, next_states = next_states, set()
    for s in prev_states:
        spots.add(s[:2])
        if s in prev:
            next_states |= prev[s]
print(len(spots))
