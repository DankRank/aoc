#!/usr/bin/env python3
import sys
import math
moons = [[int(c.split('=')[1]) for c in line.rstrip().strip('<>').split(', ')] for line in sys.stdin]
def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
def sim(x):
    n = len(x)
    x += [0]*n
    step = 0
    known = {tuple(x):step}
    while True:
        for i in range(n):
            for j in range(i+1, n):
                s = sgn(x[j] - x[i])
                x[n+i] += s
                x[n+j] -= s
        for i in range(n):
            x[i] += x[n+i]
        step += 1
        t = tuple(x)
        if t in known:
            return step - known[t], known[t]
        known[t] = step
xf, xp = sim([x[0] for x in moons])
yf, yp = sim([x[1] for x in moons])
zf, zp = sim([x[2] for x in moons])
print(min(xp, yp, zp)+math.lcm(xf, yf, zf))
