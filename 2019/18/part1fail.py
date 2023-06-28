#!/usr/bin/env python3
import sys
import string
m = [list(line.rstrip()) for line in sys.stdin]
# assumption: door always lead to previously inaccessible areas
# (i.e. no doors that can be reached from both sides, and therefore
# no need to decide whether to open a door or take a path around it)
# verified using toimage.py and GIMP bucket tool
poi = {}
objs = {}
locks = {}
for y, line in enumerate(m):
    for x, c in enumerate(line):
        if c == '@' or c in string.ascii_letters:
            if c in string.ascii_uppercase:
                locks[x, y] = c
            else:
                objs[c] = (x, y)
                poi[x, y] = c
            line[x] = '.'

key_requirements = {objs['@']: ''}
next_states = {(*objs['@'], '')}
prev_states = set()
while len(next_states):
    prev_states, next_states = next_states, set()
    for x, y, kr in prev_states:
        for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if (nx, ny) not in key_requirements and m[ny][nx] != '#':
                nkr = kr
                if (nx, ny) in locks:
                    nkr += locks[nx, ny]
                key_requirements[nx, ny] = nkr
                next_states.add((nx, ny, nkr))
keysets = {obj: set(key_requirements[pos].lower()) for obj, pos in objs.items() if obj != '@'}
keys = sorted(keysets, key=lambda x: (keysets[x], x))

dists = {}
for src in objs:
    generation = 0
    visited = {objs[src]}
    next_states = {objs[src]}
    prev_states = set()
    while len(next_states):
        prev_states, next_states = next_states, set()
        generation += 1
        for x, y in prev_states:
            for nx, ny in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if (nx, ny) not in visited and m[ny][nx] != '#':
                    if (nx, ny) in poi:
                        dists[src, poi[nx, ny]] = generation
                    visited.add((nx, ny))
                    next_states.add((nx, ny))

keytoint = {v:k for k,v in enumerate(keys)}
keytoint['@'] = -1
keysets = {keytoint[k]: sum(1<<keytoint[x] for x in v) for k, v in keysets.items()}
keysets = [v for k, v in sorted(keysets.items())]
dists = {tuple(keytoint[x] for x in k): v for k, v in dists.items()}

stack = [-1]
inventory = 0
dist = 0
mindist = float('inf')
i = 0
fullinventory = (1<<len(keys)) - 1
while True:
    while len(stack) > 1 and i == len(keys):
        i = stack.pop()
        inventory &= ~(1<<i)
        dist -= dists[stack[-1], i]
        i += 1
    if i == len(keys):
        break
    if 1<<i & inventory == 0 and inventory & keysets[i] == keysets[i]:
        ndist = dist + dists[stack[-1], i]
        if ndist >= mindist:
            i += 1
            continue
        if inventory | 1<<i == fullinventory:
            print(stack, i, ndist)
            mindist = min(ndist, mindist)
            i = len(keys)
            continue
        inventory |= 1<<i
        dist = ndist
        stack.append(i)
        i = 0
    else:
        i += 1
print(mindist)
