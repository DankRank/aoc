#!/usr/bin/env python3
import sys
bugs = frozenset((x, y) for y, line in enumerate(sys.stdin) for x, c in enumerate(line) if c == '#')
known_states = set()
def next(x, y):
    neighbors = sum(p in bugs for p in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)))
    if neighbors == 2:
        return (x, y) not in bugs
    return neighbors == 1
while bugs not in known_states:
    known_states.add(bugs)
    bugs = frozenset((x, y) for y in range(5) for x in range(5) if next(x, y))
print(sum(1<<(y*5+x) for y in range(5) for x in range(5) if (x, y) in bugs))
