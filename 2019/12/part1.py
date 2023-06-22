#!/usr/bin/env python3
import sys
moons = [[int(c.split('=')[1]) for c in line.rstrip().strip('<>').split(', ')] for line in sys.stdin]
for moon in moons:
    moon += [0, 0, 0]
def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
for i in range(1000):
    for idx, a in enumerate(moons):
        for b in moons[idx+1:]:
            s = sgn(b[0]-a[0])
            a[3] += s
            b[3] -= s
            s = sgn(b[1]-a[1])
            a[4] += s
            b[4] -= s
            s = sgn(b[2]-a[2])
            a[5] += s
            b[5] -= s
    for a in moons:
        a[0] += a[3]
        a[1] += a[4]
        a[2] += a[5]
print(sum(sum(abs(x) for x in a[:3])*sum(abs(x) for x in a[3:]) for a in moons))
