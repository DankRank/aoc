#!/usr/bin/env python3
import sys
m = [tuple(int(x) for x in line.rstrip().split(',')) for line in sys.stdin]
w, h = 71, 71

def reachable(i):
    blocked = set(m[:i])
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
    next_states = {(0, 0)}
    visited = set(next_states)
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


lo = 0
hi = len(m)
assert reachable(lo)
assert not reachable(hi)
while lo < hi-1:
    mid = (lo+hi)//2
    if reachable(mid):
        lo = mid
    else:
        hi = mid

print(','.join(str(x) for x in m[hi-1]))
