#!/usr/bin/env python3
import sys
import string
import functools
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

fullinventory = (1<<len(keys)) - 1
@functools.cache
def dfs1(pos=-1, inventory=0):
    if inventory == fullinventory:
        return 0
    mindist = float('inf')
    for i in range(len(keys)):
        if 1<<i & inventory == 0 and inventory & keysets[i] == keysets[i]:
            ndist = dists[pos, i] + dfs1(i, inventory | 1<<i)
            if ndist < mindist:
                mindist = ndist
    return mindist
print(dfs1())

for k, v in dists.items():
    if k[0] == -1 or k[1] == -1:
        dists[k] -= 2
quads = [int(objs[keys[i]][0] > objs['@'][0]) + 2*int(objs[keys[i]][1] > objs['@'][1]) for i in range(len(keys))]
@functools.cache
def dfs2(pos=(-1, -1, -1, -1), inventory=0):
    if inventory == fullinventory:
        return 0
    mindist = float('inf')
    for i in range(len(keys)):
        if 1<<i & inventory == 0 and inventory & keysets[i] == keysets[i]:
            q = quads[i]
            ndist = dists[pos[q], i] + dfs2(pos[:q]+(i,)+pos[q+1:], inventory | 1<<i)
            if ndist < mindist:
                mindist = ndist
    return mindist
print(dfs2())
