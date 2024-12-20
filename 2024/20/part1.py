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
def neighbors_cheat(s):
    x, y = s
    if 0 < x and m[y][x-1] == '#':
        yield x-1, y
    if x < w-1 and m[y][x+1] == '#':
        yield x+1, y
    if 0 < y and m[y-1][x] == '#':
        yield x, y-1
    if y < h-1 and m[y+1][x] == '#':
        yield x, y+1
def neighbors(s):
    x, y, csx, csy, cex, cey = s
    if csx is None or cex is not None:
        for nx, ny in neighbors_nocheat((x, y)):
            yield nx, ny, csx, csy, cex, cey
    else: # csx, but not cex
        for nx, ny in neighbors_nocheat((x, y)):
            yield nx, ny, csx, csy, nx, ny
    if csx is None:
        for nx, ny in neighbors_cheat((x, y)):
            yield nx, ny, x, y, None, None

def bfs1():
    next_states = {finish}
    visited = set(next_states)
    generation = 0
    dist = {finish: 0}
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

dist = bfs1()
limit = dist[start]-100

def bfs2():
    next_states = {(*start, None, None, None, None)}
    visited = set(next_states)
    generation = 0
    finish_states = set()
    while len(next_states) and generation < limit:
        generation += 1
        prev_states, next_states = next_states, set()
        for s in prev_states:
            for ns in neighbors(s):
                if ns not in visited:
                    x, y, csx, csy, cex, cey = ns
                    if cex is not None: 
                        if generation + dist[x, y] <= limit:
                            finish_states.add(ns)
                    else:
                        next_states.add(ns)
                        visited.add(ns)
                        if ns[:2] == finish:
                            finish_states.add(ns)
    return len(finish_states)
print(bfs2())
