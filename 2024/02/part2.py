#!/usr/bin/env python3
import sys
m = [[int(x) for x in line.rstrip().split()] for line in sys.stdin]
count = 0
def safe(ls):
    if ls[0] < ls[1]:
        return all(1 <= b-a <= 3 for a, b in zip(ls, ls[1:]))
    else:
        return all(-3 <= b-a <= -1 for a, b in zip(ls, ls[1:]))
for ls in m:
    if safe(ls):
        count += 1
    else:
        for i in range(len(ls)):
            if safe(ls[:i]+ls[i+1:]):
                count += 1
                break
print(count)
