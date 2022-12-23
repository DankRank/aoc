#!/usr/bin/env python3
import sys
from collections import Counter
elves = set((x, y) for y, line in enumerate(sys.stdin.read().splitlines()) for x, c in enumerate(line) if c == '#')
i = 0
while True:
    proposed = {}
    for x, y in elves:
        NW = (x-1, y-1) in elves
        N  = (x,   y-1) in elves
        NE = (x+1, y-1) in elves
        W  = (x-1, y  ) in elves
        E  = (x+1, y  ) in elves
        SW = (x-1, y+1) in elves
        S  = (x,   y+1) in elves
        SE = (x+1, y+1) in elves
        if not (NW or N or NE or W or E or SW or S or SE):
            proposed[(x, y)] = (x, y)
        else:
            for j in range(4):
                if (i+j)%4 == 0:
                    if not (NW or N or NE):
                        proposed[(x, y)] = (x, y-1)
                        break
                elif (i+j)%4 == 1:
                    if not (SW or S or SE):
                        proposed[(x, y)] = (x, y+1)
                        break
                elif (i+j)%4 == 2:
                    if not (NW or W or SW):
                        proposed[(x, y)] = (x-1, y)
                        break
                elif (i+j)%4 == 3:
                    if not (NE or E or SE):
                        proposed[(x, y)] = (x+1, y)
                        break
            else:
                proposed[(x, y)] = (x, y)
    ctr = Counter(proposed.values())
    nelves = set()
    for x, y in elves:
        if ctr[proposed[(x, y)]] == 1:
            nelves.add(proposed[(x, y)])
        else:
            nelves.add((x, y))
    if elves == nelves:
        break
    elves = nelves
    i += 1
print(i+1)
