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

minx = min(c[0] for c in cubes)
miny = min(c[1] for c in cubes)
minz = min(c[2] for c in cubes)
maxx = max(c[0] for c in cubes)
maxy = max(c[1] for c in cubes)
maxz = max(c[2] for c in cubes)

init_state = (minx-1, miny-1, minz-1)
known_states = {init_state}
prev_states = set()
next_states = {init_state}
while True:
    prev_states, next_states = next_states, set()
    if len(prev_states) == 0:
        break
    for c in prev_states:
        for c2 in neighbors(c):
            if c2[0] >= minx-1 and c2[1] >= miny-1 and c2[2] >= minz-1:
                if c2[0] <= maxx+1 and c2[1] <= maxy+1 and c2[2] <= maxz+1:
                    if c2 not in known_states and c2 not in cubes:
                        known_states.add(c2)
                        next_states.add(c2)

count = 0
for c in cubes:
    for c2 in neighbors(c):
        if c2 in known_states:
            count += 1
print(count)
