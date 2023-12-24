#!/usr/bin/env python3
import sys
from fractions import Fraction
m = [[tuple(int(x) for x in s.split(', ')) for s in line.rstrip().split(' @ ')] for line in sys.stdin]
for line in m:
    assert all(line[1])

testarea = range(200000000000000, 400000000000000+1)

lines = []
for u, v in m:
    # turn line into a function ax + b
    a = Fraction(v[1], v[0])
    # b = y - ax
    b = u[1] - a*u[0]
    lines.append((a, b))

count = 0
for i, u in enumerate(m):
    for j, v in enumerate(m[i+1:], i+1):
        if lines[i] == lines[j]:
            # there are a few situations here
            # 1) lines don't intersect testarea
            # 2) lines do intersect testarea, but the rays don't
            # 3) rays intersect the test area
            assert False
        else:
            # ax + b = cx + d
            # (a-c)x = d-b
            # x = (d-b)/(a-c), assuming a!=c (line aren't parallel)
            a, b = lines[i]
            c, d = lines[j]
            if a == c:
                continue
            x = (d-b)/(a-c)
            y = a*x + b
            # check that the point is on the correct side of both rays
            if (x > u[0][0]) != (u[1][0] > 0):
                continue
            if (x > v[0][0]) != (v[1][0] > 0):
                continue
            if testarea.start <= x < testarea.stop and testarea.start <= y < testarea.stop:
                count += 1
print(count)
