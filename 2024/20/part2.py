#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)

for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch == 'S':
            start = (x, y)
        elif ch == 'E':
            finish = (x, y)

def neighbors_nocheat(s):
    x, y = s
    if 0 < x and m[y][x-1] != '#':
        yield x-1, y
    if x < w-1 and m[y][x+1] != '#':
        yield x+1, y
    if 0 < y and m[y-1][x] != '#':
        yield x, y-1
    if y < h-1 and m[y+1][x] != '#':
        yield x, y+1

def bfs1(init):
    next_states = {init}
    visited = set(next_states)
    generation = 0
    dist = {init: 0}
    while len(next_states):
        generation += 1
        prev_states, next_states = next_states, set()
        for s in prev_states:
            for ns in neighbors_nocheat(s):
                if ns not in visited:
                    next_states.add(ns)
                    visited.add(ns)
                    dist[ns] = generation
    return dist

dist1 = bfs1(start)
dist2 = bfs1(finish)
limit = dist1[finish]-100

count = 0
for (csx, csy), d1 in dist1.items():
    for (cex, cey), d2 in dist2.items():
        if d1 + d2 <= limit:
            d3 = abs(cex-csx) + abs(cey-csy)
            if d3 <= 20:
                if d1 + d3 +  d2 <= limit:
                    count += 1
print(count)
