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

ks2 = {obj: key_requirements[pos].lower() for obj, pos in objs.items() if obj != '@'}
ks3 = {}
for k, v in ks2.items():
    if v not in ks3:
        ks3[v] = []
    ks3[v].append(k)
pareas = {}
for k in ks3:
    while len(k) > 1:
        pareas[k[-1]] = k[-2]
        k = k[:-1]
    if len(k):
        pareas[k] = ''
print("digraph {")
for k, v in ks3.items():
    v = ', '.join(v)
    print(f'"{k[-1:]}" [label="{v}"]')
for k, v in pareas.items():
    print(f'"{v}" -> "{k}" [label="{k}"]')
print("}")
