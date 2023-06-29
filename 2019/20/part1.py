#!/usr/bin/env python3
import sys
m = [list(line.rstrip('\n')) for line in sys.stdin]

portals = {}
aa = None
zz = None
tmp = {}
def addportal(wallx, wally, floorx, floory):
    global aa, zz
    if wallx == floorx:
        if wally < floory:
            label = m[wally-1][wallx] + m[wally][wallx]
        else:
            label = m[wally][wallx] + m[wally+1][wallx]
    else:
        if wallx < floorx:
            label = m[wally][wallx-1] + m[wally][wallx]
        else:
            label = m[wally][wallx] + m[wally][wallx+1]

    if label == 'AA':
        m[wally][wallx] = '#'
        aa = floorx, floory
    elif label == 'ZZ':
        m[wally][wallx] = '#'
        zz = floorx, floory
    else:
        m[wally][wallx] = '.'
        if label not in tmp:
            tmp[label] = ((wallx, wally), (floorx, floory))
        else:
            otherwall, otherfloor = tmp[label]
            portals[wallx, wally] = otherfloor
            portals[otherwall] = floorx, floory

w, h = len(m[0]), len(m)
for i in range(len(m[0])):
    if m[0][i] != ' ':
        addportal(i, 1, i, 2)
    if m[-2][i] != ' ':
        addportal(i, h-2, i, h-3)
for i in range(len(m)):
    if m[i][0] != ' ':
        addportal(1, i, 2, i)
    if m[i][-2] != ' ':
        addportal(w-2, i, w-3, i)

minx = None
miny = None
for i in range(2,len(m)-2):
    if ' ' in m[i][2:-2]:
        if miny is None:
            miny = i
        maxy = i+1
for i in range(2,len(m[miny])-2):
    if m[miny][i] == ' ':
        if minx is None:
            minx = i
        maxx = i+1

for i in range(minx, maxx):
    if m[miny][i] != ' ':
        addportal(i, miny, i, miny-1)
    if m[maxy-2][i] != ' ':
        addportal(i, maxy-1, i, maxy)
for i in range(miny, maxy):
    if m[i][minx] != ' ':
        addportal(minx, i, minx-1, i)
    if m[i][maxx-2] != ' ':
        addportal(maxx-1, i, maxx, i)

generation = 0
known_states = {(x, y) for y, i in enumerate(m) for x, j in enumerate(i) if j == '#'}
next_states = {aa}
prev_states = set()
while zz not in known_states:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for x, y in prev_states:
        for ns in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            if ns in portals:
                ns = portals[ns]
            if ns not in known_states:
                next_states.add(ns)
                known_states.add(ns)
print(generation)
