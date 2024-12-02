#!/usr/bin/env python3
import sys
m = [[int(x) for x in line.rstrip().split()] for line in sys.stdin]
count = 0
for ls in m:
    if ls[0] < ls[1]:
        if all(1 <= b-a <= 3 for a, b in zip(ls, ls[1:])):
            count += 1
    else:
        if all(-3 <= b-a <= -1 for a, b in zip(ls, ls[1:])):
            count += 1
print(count)
