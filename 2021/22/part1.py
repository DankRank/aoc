#!/usr/bin/env python3
cuboids = []
try:
    while True:
        a, b = input().split()
        cuboids.append((tuple(map(lambda x: tuple(map(int, x.split('=')[1].split('..'))), b.split(','))), True if a == 'on' else False))
except EOFError:
    pass

def clamprange(x, minx, maxx):
    return range(max(minx, x[0]), min(maxx, x[1])+1)

grid = set()
for coords, val in cuboids:
    for i in clamprange(coords[0], -50, 50):
        for j in clamprange(coords[1], -50, 50):
            for k in clamprange(coords[2], -50, 50):
                if val:
                    grid.add((i, j, k))
                else:
                    grid.discard((i, j, k))
print(sum(1 for i in range(-50, 51) for j in range(-50, 51) for k in range(-50, 51) if (i, j, k) in grid))
