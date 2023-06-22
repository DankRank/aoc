#!/usr/bin/env python3
import sys
m = {}
for line in sys.stdin:
    lhs, rhs = line.rstrip().split(' => ')
    lhs = [(b, int(a)) for a, b in (tuple(ing.split()) for ing in lhs.split(', '))]
    count, prod = rhs.split()
    assert prod not in m
    m[prod] = (int(count), lhs)
orelast = 0
slast = {k:0 for k in m}
fuel = 0
step = 1000000
while step:
    ore, s = orelast, slast.copy()
    fuel += step
    s['FUEL'] -= step
    while any(i < 0 for i in s.values()):
        for k in list(s):
            if s[k] < 0:
                factor = (-s[k]+m[k][0]-1)//m[k][0]
                s[k] += m[k][0]*factor
                for ing, count in m[k][1]:
                    if ing == 'ORE':
                        ore += count*factor
                    else:
                        s[ing] -= count*factor
    if ore <= 1000000000000:
        orelast, slast = ore, s
    else:
        fuel -= step
        step //= 10
print(fuel)
