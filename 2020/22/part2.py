#!/usr/bin/env python3
from collections import deque
from itertools import islice
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

# True = P1, False = P2
def game(d1, d2):
    seen1 = set()
    seen2 = set()
    while len(d1) != 0 and len(d2) != 0:
        t1 = tuple(d1)
        t2 = tuple(d2)
        if t1 in seen1 or t2 in seen2:
            return True
        seen1.add(t1)
        seen2.add(t2)

        c1 = d1.popleft()
        c2 = d2.popleft()
        if c1 <= len(d1) and c2 <= len(d2):
            cond = game(deque(islice(d1, c1)), deque(islice(d2, c2)))
        else:
            cond = c1 > c2
        if cond:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    return len(d1) != 0

winner = d1 if game(d1, d2) else d2
total = 0
for i,c in zip(range(len(winner)),reversed(winner)):
    total += c * (i+1)
print(total)

