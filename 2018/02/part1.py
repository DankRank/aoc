#!/usr/bin/env python3
import sys
from collections import Counter
m = [line.rstrip() for line in sys.stdin]

count2 = 0
count3 = 0
for line in m:
    counts = set(Counter(line).values())
    if 2 in counts:
        count2 += 1
    if 3 in counts:
        count3 += 1
print(count2*count3)

def find():
    for i in range(len(m[0])):
        seen = set()
        for line in m:
            line = line[:i]+line[i+1:]
            if line in seen:
                return line
            seen.add(line)
print(find())
