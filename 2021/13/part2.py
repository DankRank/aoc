#!/usr/bin/env python3
dots = set()
while True:
    line = input()
    if line == '':
        break
    x, y = map(int, line.split(','))
    dots.add((x,y))
try:
    while True:
        axis, coord = input().split()[2].split('=')
        axis = 0 if axis == 'x' else 1
        coord = int(coord)
        ndots = set()
        for dot in dots:
            if dot[axis] < coord:
                ndots.add(dot)
            elif dot[axis] > coord:
                nc = coord - (dot[axis] - coord)
                ndots.add((nc, dot[1]) if axis == 0 else (dot[0], nc))
        dots = ndots
except EOFError:
    pass
minx = min(x for x,y in dots)
maxx = max(x for x,y in dots)
miny = min(y for x,y in dots)
maxy = max(y for x,y in dots)
for y in range(miny, maxy+1):
    print("".join('#' if (x,y) in dots else ' ' for x in range(minx, maxx+1)))
