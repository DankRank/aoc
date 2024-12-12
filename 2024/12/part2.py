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
        del regions[r2]
def add(pos1, pos2, perimeter):
    r1 = toregion[pos1]
    toregion[pos2] = r1
    regions[r1][0].add(pos2)
    regions[r1][1] += perimeter

for y in range(h):
    for x in range(w):
        perimeter = 0
        left = x > 0 and m[y][x-1] == m[y][x]
        right = x < w-1 and m[y][x+1] == m[y][x]
        up = y > 0 and m[y-1][x] == m[y][x]
        down = y < h-1 and m[y+1][x] == m[y][x]
        upleft = x > 0 and y > 0 and m[y-1][x-1] == m[y][x]
        upright = x < w-1 and y > 0 and m[y-1][x+1] == m[y][x]
        downleft = x > 0 and y < h-1 and m[y+1][x-1] == m[y][x]
        if not up and not (left and not upleft):
            perimeter += 1
        if not down and not (left and not downleft):
            perimeter += 1
        if not left and not (up and not upleft):
            perimeter += 1
        if not right and not (up and not upright):
            perimeter += 1
        if up:
            if left:
                merge((x, y-1), (x-1, y))
            add((x, y-1), (x, y), perimeter)
        elif left:
            add((x-1, y), (x, y), perimeter)
        else:
            regions[(x, y)] = [{(x, y)}, perimeter]
            toregion[(x, y)] = (x, y)
print(sum(b*len(a) for a, b in regions.values()))
