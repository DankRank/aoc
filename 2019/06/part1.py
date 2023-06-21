#!/usr/bin/env python3
import sys
m = {b:a for a,b in (line.rstrip().split(')') for line in sys.stdin)}
assert 'COM' not in m
solved = {'COM': 0}
def solve(k):
    if k not in solved:
        solved[k] = 1+solve(m[k])
    return solved[k]
for k in m:
    solve(k)
print(sum(solved.values()))
