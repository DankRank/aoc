#!/usr/bin/env python3
import sys
from collections import Counter
m = [tuple(int(x) for x in line.rstrip().split(',')) for line in sys.stdin]

minx, maxx, miny, maxy = float('inf'), float('-inf'), float('inf'), float('-inf')
for x, y in m:
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y

def neighbors(s):
    x, y = s
    if x > minx:
        yield x-1, y
    if x < maxx:
        yield x+1, y
    if y > miny:
        yield x, y-1
    if y < maxy:
        yield x, y+1

owners = {(x, y): (x, y) for x, y in m}
owncount = Counter(m)

next_states = set(m)
while len(next_states):
    prev_states, next_states = next_states, set()
    for s in prev_states:
        owner = owners[s]
        for ns in neighbors(s):
            if ns in next_states and owners[ns] != owner:
                old_owner, owners[ns] = owners[ns], None
                owncount[old_owner] -= 1
            elif ns not in owners:
                next_states.add(ns)
                owners[ns] = owner
                owncount[owner] += 1

edgeowners = set()
def edges():
    for x in range(minx, maxx+1):
        yield x, miny
        yield x, maxy
    for y in range(miny+1, maxy):
        yield minx, y
        yield maxx, y
for x, y in edges():
    if owners[x, y] is not None:
        edgeowners.add(owners[x, y])

del owncount[None]

print(max(v for k, v in owncount.items() if k not in edgeowners))
