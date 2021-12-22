#!/usr/bin/env python3
from itertools import chain
cuboids = []
try:
    while True:
        a, b = input().split()
        cuboids.append((tuple(map(lambda x: tuple(map(int, x.split('=')[1].split('..'))), b.split(','))), True if a == 'on' else False))
except EOFError:
    pass

def valid(c):
    return c[0][0] <= c[0][1] and c[1][0] <= c[1][1] and c[2][0] <= c[2][1]

def intersect(c1, c2):
    if any(c1[i][1] < c2[i][0] or c1[i][0] > c2[i][1] for i in range(3)):
        return [c2]
    c3 = tuple((max(c1[i][0], c2[i][0]), min(c1[i][1], c2[i][1])) for i in range(3))
    return filter(valid, [
            ((c2[0][0], c3[0][0]-1), c2[1], c2[2]),
            ((c3[0][1]+1, c2[0][1]), c2[1], c2[2]),
            (c3[0], (c2[1][0], c3[1][0]-1), c2[2]),
            (c3[0], (c3[1][1]+1, c2[1][1]), c2[2]),
            (c3[0], c3[1], (c2[2][0], c3[2][0]-1)),
            (c3[0], c3[1], (c3[2][1]+1, c2[2][1]))
        ])

newcuboids = []
for c1, val in cuboids:
    newcuboids = list(chain.from_iterable(map(lambda c2: intersect(c1, c2), newcuboids)))
    if val:
        newcuboids.append(c1)
print(sum((c[0][1]-c[0][0]+1) * (c[1][1]-c[1][0]+1) * (c[2][1]-c[2][0]+1) for c in newcuboids))
