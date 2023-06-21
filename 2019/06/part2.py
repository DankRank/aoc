#!/usr/bin/env python3
import sys
m = {b:a for a,b in (line.rstrip().split(')') for line in sys.stdin)}
assert 'COM' not in m
def rootpath(k):
    p = []
    while k != 'COM':
        k = m[k]
        p.append(k)
    p.reverse()
    return p
a = rootpath('YOU')
b = rootpath('SAN')
i = 0
while a[i] == b[i]:
    i += 1
print(len(a) + len(b) - 2*i)
