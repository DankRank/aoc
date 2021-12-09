#!/usr/bin/env python3
heightmap = []
try:
    while True:
        heightmap.append(list(map(int, input())))
except EOFError:
    pass

def getNeighbors(y,x):
    if x != 0:
        yield heightmap[y][x-1]
    if x != len(heightmap[y])-1:
        yield heightmap[y][x+1]
    if y != 0:
        yield heightmap[y-1][x]
    if y != len(heightmap)-1:
        yield heightmap[y+1][x]

risk = 0
for i in range(len(heightmap)):
    for j in range(len(heightmap)):
        if all(x > heightmap[i][j] for x in getNeighbors(i, j)):
            risk += 1 + heightmap[i][j]
print(risk)
