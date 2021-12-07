#!/usr/bin/env python3
from statistics import median
pos = list(map(int, input().split(',')))
median = round(median(pos))
print(sum(abs(x-median) for x in pos))
