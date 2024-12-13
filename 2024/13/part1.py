#!/usr/bin/env python3
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
        a = px*by + py*-bx
        b = px*-ay + py*ax
        if a % det or b % det:
            continue
        count += (3*a + b) // det
    return count

print(solve())
for line in m:
    line[4] += 10000000000000
    line[5] += 10000000000000
print(solve())

