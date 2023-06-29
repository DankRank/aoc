#!/usr/bin/env python3
import sys
bugs = frozenset((x, y, 0) for y, line in enumerate(sys.stdin) for x, c in enumerate(line) if c == '#')
def neighbors(x, y, d):
    if x == 1 and y == 2: # left of center
        yield 0, 2, d
        yield 1, 1, d
        yield 1, 3, d
        for i in range(5):
            yield 0, i, d+1
    elif x == 3 and y == 2: # right of center
        yield 4, 2, d
        yield 3, 1, d
        yield 3, 3, d
        for i in range(5):
            yield 4, i, d+1
    elif x == 2 and y == 1: # top of center
        yield 2, 0, d
        yield 1, 1, d
        yield 3, 1, d
        for i in range(5):
            yield i, 0, d+1
    elif x == 2 and y == 3: # bottom of center
        yield 2, 4, d
        yield 1, 3, d
        yield 3, 3, d
        for i in range(5):
            yield i, 4, d+1
    else:
        if x == 0: # left outside
            yield 1, 2, d-1
        else:
            yield x-1, y, d
        if x == 4: # right outside
            yield 3, 2, d-1
        else:
            yield x+1, y, d
        if y == 0: # top outside
            yield 2, 1, d-1
        else:
            yield x, y-1, d
        if y == 4: # bottom outside
            yield 2, 3, d-1
        else:
            yield x, y+1, d
def next(x, y, d):
    n = sum(p in bugs for p in neighbors(x, y, d))
    if n == 2:
        return (x, y, d) not in bugs
    return n == 1
for i in range(200):
    mind = min(d for x, y, d in bugs)
    maxd = max(d for x, y, d in bugs)
    bugs = frozenset((x, y, d) for y in range(5) for x in range(5) for d in range(mind-1, maxd+2) if (x != 2 or y != 2) and next(x, y, d))
print(len(bugs))
