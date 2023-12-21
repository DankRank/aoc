#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin] 
rocks = {(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == '#'}
start = [(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'S'][0]
w, h = len(m[0]), len(m)
def neighbors(s):
    if s[0] > 0   and (s[0]-1, s[1]) not in rocks:
        yield s[0]-1, s[1]
    if s[0] < w-1 and (s[0]+1, s[1]) not in rocks:
        yield s[0]+1, s[1]
    if s[1] > 0   and (s[0], s[1]-1) not in rocks:
        yield s[0], s[1]-1
    if s[1] < h-1 and (s[0], s[1]+1) not in rocks:
        yield s[0], s[1]+1
prev_states, next_states = set(), {start}
generation = 0
while generation != 64:
    prev_states, next_states = next_states, set()
    generation += 1
    for s in prev_states:
        for ns in neighbors(s):
            next_states.add(ns)
print(len(next_states))
