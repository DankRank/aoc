#!/usr/bin/env python3
import sys
m = [[int(x) for x in line.rstrip()] for line in sys.stdin]
w, h = len(m[0]), len(m)

def neighbors(x, y, i):
    if 0 < x and m[y][x-1] == i:
        yield x-1, y
    if x < w-1 and m[y][x+1] == i:
        yield x+1, y
    if 0 < y and m[y-1][x] == i:
        yield x, y-1
    if y < h-1 and m[y+1][x] == i:
        yield x, y+1

next_states = set()
for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch == 0:
            next_states.add(((x, y), x, y))
generation = 0
while generation < 9:
    generation += 1
    prev_states, next_states = next_states, set()
    for tag, x, y in prev_states:
        for nx, ny in neighbors(x, y, generation):
            next_states.add((tag, nx, ny))
print(len(next_states))
