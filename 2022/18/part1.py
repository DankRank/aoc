#!/usr/bin/env python3
cubes = set()
try:
    while True:
        cubes.add(tuple(int(s) for s in input().split(',')))
except EOFError:
    pass
def neighbors(c):
    yield c[0]-1, c[1], c[2]
    yield c[0]+1, c[1], c[2]
    yield c[0], c[1]-1, c[2]
    yield c[0], c[1]+1, c[2]
    yield c[0], c[1], c[2]-1
    yield c[0], c[1], c[2]+1
count = 0
for c in cubes:
    for c2 in neighbors(c):
        if c2 not in cubes:
            count += 1
print(count)
