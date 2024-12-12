#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)

regions = {}
toregion = {}
def merge(pos1, pos2):
    r1 = toregion[pos1]
    r2 = toregion[pos2]
    if r1 != r2:
        for pos in regions[r2][0]:
            toregion[pos] = r1
        regions[r1][0] |= regions[r2][0]
        regions[r1][1] += regions[r2][1]
        regions[r1][2] += regions[r2][2]
        del regions[r2]
def add(pos1, pos2, perimeter):
    r1 = toregion[pos1]
    toregion[pos2] = r1
    regions[r1][0].add(pos2)
    regions[r1][1] += perimeter
    regions[r1][2] += 1

for y in range(h):
    for x in range(w):
        perimeter = 4
        left = False
        up = False
        if x > 0 and m[y][x-1] == m[y][x]:
            left = True
            perimeter -= 1
        if x < w-1 and m[y][x+1] == m[y][x]:
            perimeter -= 1
        if y > 0 and m[y-1][x] == m[y][x]:
            up = True
            perimeter -= 1
        if y < h-1 and m[y+1][x] == m[y][x]:
            perimeter -= 1
        if up:
            if left:
                merge((x, y-1), (x-1, y))
            add((x, y-1), (x, y), perimeter)
        elif left:
            add((x-1, y), (x, y), perimeter)
        else:
            regions[(x, y)] = [{(x, y)}, perimeter, 1]
            toregion[(x, y)] = (x, y)
print(sum(b*c for a, b, c in regions.values()))
