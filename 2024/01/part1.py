#!/usr/bin/env python3
import sys
m = [[int(x) for x in line.rstrip().split()] for line in sys.stdin]
m = [sorted(x) for x in zip(*m)]
print(sum(abs(a-b) for a, b in zip(*m)))
print(sum(a*m[1].count(a) for a in m[0]))
