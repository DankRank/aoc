#!/usr/bin/env python3
from fractions import Fraction
m = []
try:
    while True:
        ax, ay = (int(x.split('+')[1]) for x in input().split(': ')[1].split(', '))
        bx, by = (int(x.split('+')[1]) for x in input().split(': ')[1].split(', '))
        px, py = (int(x.split('=')[1]) for x in input().split(': ')[1].split(', '))
        m.append([ax, ay, bx, by, px, py])
        input()
except EOFError:
    pass

def solve():
    count = 0
    for ax, ay, bx, by, px, py in m:
        det = ax*by - bx*ay
        idet = Fraction(1, det)
        a = px*by*idet + py*-bx*idet
        b = px*-ay*idet + py*ax*idet
        if a.denominator != 1 or b.denominator != 1:
            continue
        count += 3*a + b
    return count

print(solve())
for line in m:
    line[4] += 10000000000000
    line[5] += 10000000000000
print(solve())

