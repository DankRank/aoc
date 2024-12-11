#!/usr/bin/env python3
m = [int(x) for x in input().split()]

def step(m):
    n = []
    for x in m:
        if x == 0:
            n.append(1)
        else:
            digits = len(str(x))
            if digits % 2 == 0:
                n += divmod(x, 10**(digits//2))
            else:
                n.append(2024*x)
    return n

for i in range(25):
    m = step(m)
print(len(m))
