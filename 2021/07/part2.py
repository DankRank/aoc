#!/usr/bin/env python3
from statistics import mean
pos = list(map(int, input().split(',')))
def trinum(n):
    return n*(n+1)//2
avg = int(mean(pos))
print(min(sum(trinum(abs(x-(avg+i))) for x in pos) for i in range(2)))
# Centroid of a set of points minimizes the sum of squared distances to the points.
# I'm pretty sure it also works for any quadratic polynomial of distances, as long
# as the polynomial is monotonic increasing for x > 0 (i.e. a > 0, b >= 0). This is
# the case for triangular numbers.
