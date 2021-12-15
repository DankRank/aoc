#!/usr/bin/env python3
from heapq import heappush, heappop
grid = []
try:
    while True:
        grid.append(list(map(int, input())))
except EOFError:
    pass
w = len(grid)

ngrid = []
for i2 in range(5):
    for i in range(w):
        row = []
        for j2 in range(5):
            for j in range(w):
                row.append((grid[i][j] + i2 + j2 - 1)%9 + 1)
        ngrid.append(row)
grid = ngrid
w *= 5

def neighbors(i,j):
    if i != 0:
        yield i-1, j
    if j != 0:
        yield i, j-1
    if i != w-1:
        yield i+1, j
    if j != w-1:
        yield i, j+1

maxval = w*w*9 + 1
dist = {(i,j): maxval for i in range(w) for j in range(w)}
q = []
dist[0,0] = 0
heappush(q, (0, 0, 0))
while len(q) > 0:
    d, i, j = heappop(q)
    if d == dist[i, j]:
        for x, y in neighbors(i, j):
            ndist = dist[i, j] + grid[x][y]
            if ndist < dist[x, y]:
                dist[x, y] = ndist
                heappush(q, (dist[x, y], x, y))
print(dist[w-1, w-1])
