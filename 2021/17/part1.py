#!/usr/bin/env python3
_, _, xstr, ystr = input().split()
minx, maxx = map(int, xstr[2:-1].split('..'))
miny, maxy = map(int, ystr[2:].split('..'))
def check(v0):
    y = 0
    v = v0
    while True:
        if y < miny:
            return False
        if y <= maxy:
            return True
        y += v
        v -= 1
def maxheight(v0):
    maxh = 0
    y = 0
    v = v0
    while v >= 0:
        if y > maxh:
            maxh = y
        y += v
        v -= 1
    return maxh
# wow this is really terrible
print(max(maxheight(i) for i in range(200) if check(i)))
