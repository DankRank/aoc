#!/usr/bin/env python3
from operator import mul
from functools import reduce
heightmap = []
try:
    while True:
        heightmap.append(list(map(int, input())))
except EOFError:
    pass

seen = set()
basins = []

def getNeighbors(y,x):
    if x != 0                   and (y, x-1) not in seen and heightmap[y][x-1] != 9:
        yield y, x-1
    if x != len(heightmap[y])-1 and (y, x+1) not in seen and heightmap[y][x+1] != 9:
        yield y, x+1
    if y != 0                   and (y-1, x) not in seen and heightmap[y-1][x] != 9:
        yield y-1, x
    if y != len(heightmap)-1    and (y+1, x) not in seen and heightmap[y+1][x] != 9:
        yield y+1, x

def floodFill(y,x):
    count = 0
    queue = set()
    queue.add((y,x))
    while len(queue) > 0:
        coord = queue.pop()
        if coord not in seen:
            queue.update(getNeighbors(*coord))
            seen.add(coord)
            count += 1
    return count

for i in range(len(heightmap)):
    for j in range(len(heightmap)):
        if (i, j) not in seen:
            if heightmap[i][j] != 9:
                basins.append(floodFill(i,j))
            else:
                seen.add((i, j))
print(reduce(mul, sorted(basins)[-3:]))
