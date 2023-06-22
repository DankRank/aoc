#!/usr/bin/env python3
import sys
m = {}
for line in sys.stdin:
    lhs, rhs = line.rstrip().split(' => ')
    lhs = [(b, int(a)) for a, b in (tuple(ing.split()) for ing in lhs.split(', '))]
    count, prod = rhs.split()
    assert prod not in m
    m[prod] = (int(count), lhs)
ore = 0
s = {k:0 for k in m}
s['FUEL'] -= 1
while any(i < 0 for i in s.values()):
    for k in list(s):
        while s[k] < 0:
            s[k] += m[k][0]
            for ing, count in m[k][1]:
                if ing == 'ORE':
                    ore += count
                else:
                    s[ing] -= count
print(ore)
    
