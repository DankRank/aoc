#!/usr/bin/env python3
from intcode import *
tiles = set()
visited = set()
x, y = 0, 0
dx, dy = 0, -1
vm = IntcodeVM(parsetext(input()))
while not vm.halted:
    vm.inq.append(int((x, y) in tiles))
    vm.run()
    visited.add((x, y))
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
print(len(visited))
