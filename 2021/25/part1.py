#!/usr/bin/env python3
grid = []
try:
    while True:
        grid.append(list(input()))
except EOFError:
    pass

h = len(grid)
w = len(grid[0])

rightset = set()
downset = set()

for y in range(h):
    for x in range(w):
        if grid[y][x] == '>':
            rightset.add((x, y))
        elif grid[y][x] == 'v':
            downset.add((x, y))

def step(rightset, downset):
    nrightset = set()
    for x, y in rightset:
        ncoord = (x+1)%w, y
        if ncoord in rightset or ncoord in downset:
            nrightset.add((x, y))
        else:
            nrightset.add(ncoord)

    ndownset = set()
    for x, y in downset:
        ncoord = x, (y+1)%h
        if ncoord in nrightset or ncoord in downset:
            ndownset.add((x, y))
        else:
            ndownset.add(ncoord)
    return nrightset, ndownset

count = 1
while True:
    orightset, odownset, rightset, downset, = rightset, downset, *step(rightset, downset)
    if orightset == rightset and odownset == downset:
        break
    count += 1
print(count)
