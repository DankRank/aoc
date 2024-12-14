#!/usr/bin/env python3
import sys
from functools import reduce
from operator import mul
m = [tuple(tuple(int(x) for x in pair.split('=')[1].split(',')) for pair in line.rstrip().split()) for line in sys.stdin]
w, h = 101, 103
#w, h = 11, 7
counts = [0]*4
for (px, py), (vx, vy) in m:
    x = (px + vx*100) % w
    y = (py + vy*100) % h
    if x == w//2 or y == h//2:
        continue
    q = 0
    if x > w//2:
        q += 1
    if y > h//2:
        q += 2
    counts[q] += 1
print(reduce(mul, counts))
