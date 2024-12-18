#!/usr/bin/env python3
import sys
m = [tuple(int(x) for x in line.rstrip().split(',')) for line in sys.stdin]
w, h = 71, 71

blocked = set()
def neighbors(s):
    x, y = s
    if 0 < x and (x-1, y) not in blocked:
        yield x-1, y
    if x < w-1 and (x+1, y) not in blocked:
        yield x+1, y
    if 0 < y and (x, y-1) not in blocked:
        yield x, y-1
    if y < h-1 and (x, y+1) not in blocked:
        yield x, y+1

def reachable():
    next_states = {(0, 0)}
    visited = set()
    generation = 0
    while len(next_states):
        if (w-1, h-1) in next_states:
            return True
        generation += 1
        prev_states, next_states = next_states, set()
        for s in prev_states:
            for ns in neighbors(s):
                if ns not in visited:
                    next_states.add(ns)
                    visited.add(ns)
    return False

i = 1024
blocked.update(m[:1024])
while reachable():
    blocked.add(m[i])
    i += 1
print(','.join(str(x) for x in m[i-1]))
set
