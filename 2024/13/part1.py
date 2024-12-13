#!/usr/bin/env python3
import functools
import sys
sys.setrecursionlimit(10000)
m = []
try:
    while True:
        ax, ay = (int(x.split('+')[1]) for x in input().split(': ')[1].split(', '))
        bx, by = (int(x.split('+')[1]) for x in input().split(': ')[1].split(', '))
        px, py = (int(x.split('=')[1]) for x in input().split(': ')[1].split(', '))
        m.append((ax, ay, bx, by, px, py))
        input()
except EOFError:
    pass

@functools.cache
def rec(ax, ay, bx, by, px, py):
    if px == 0 and py == 0:
        return 0
    res1, res2 = None, None
    if ax <= px and ay <= py:
        res1 = rec(ax, ay, bx, by, px-ax, py-ay)
    if bx <= px and by <= py:
        res2 = rec(ax, ay, bx, by, px-bx, py-by)
    if res1 is None:
        if res2 is None:
            return None
        else:
            return 1+res2
    else:
        if res2 is None:
            return 3+res1
        else:
            return min(3+res1, 1+res2)

print(sum(rec(*params) or 0 for params in m))

