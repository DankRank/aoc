#!/usr/bin/env python3
from collections import deque
import sys

def parse(infile):
    d1 = deque()
    d2 = deque()
    infile.readline() # skip "Player 1:"
    for line in infile:
        line = line.rstrip()
        if line == '':
            break
        d1.append(int(line))
    infile.readline() # skip "Player 2:"
    for line in infile:
        d2.append(int(line.rstrip()))
    return d1, d2

d1, d2 = parse(sys.stdin)

while len(d1) != 0 and len(d2) != 0:
    c1 = d1.popleft()
    c2 = d2.popleft()
    if c1 > c2:
        d1.append(c1)
        d1.append(c2)
    else:
        d2.append(c2)
        d2.append(c1)

winner = d1 if len(d1) != 0 else d2
total = 0
for i,c in zip(range(len(winner)),reversed(winner)):
    total += c * (i+1)
print(total)

