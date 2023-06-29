#!/usr/bin/env python3
from intcode import *
tiles = {(0, 0)}
x, y = 0, 0
dx, dy = 0, -1
vm = IntcodeVM(parsetext(input()))
while not vm.halted:
    vm.inq.append(int((x, y) in tiles))
    vm.run()
    if vm.outq.pop(0) != 0:
        tiles.add((x, y))
    else:
        tiles.discard((x, y))
    if vm.outq.pop(0) != 0:
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    x += dx
    y += dy
minx = min(tiles, key=lambda x: x[0])[0]
maxx = max(tiles, key=lambda x: x[0])[0]
miny = min(tiles, key=lambda x: x[1])[1]
maxy = max(tiles, key=lambda x: x[1])[1]
for y in range(miny, maxy+1):
    line = []
    for x in range(minx, maxx+1):
        line.append('#' if (x, y) in tiles else ' ')
    print(''.join(line))
