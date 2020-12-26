#!/usr/bin/env python3
import itertools, sys, pprint

xfrm = (
    lambda x,y: (  x,  y),
    lambda x,y: (9-x,  y),
    lambda x,y: (  x,9-y),
    lambda x,y: (9-x,9-y),
    lambda x,y: (  y,  x),
    lambda x,y: (  y,9-x),
    lambda x,y: (9-y,  x),
    lambda x,y: (9-y,9-x))
comp = (
    (0,1,2,3,4,5,6,7),
    (1,0,3,2,5,4,7,6),
    (2,3,0,1,6,7,4,5),
    (3,2,1,0,7,6,5,4),
    (4,6,5,7,0,2,1,3),
    (5,7,4,6,1,3,0,2),
    (6,4,7,5,2,0,3,1),
    (7,5,6,4,3,1,2,0))

r0 = 0
m1 = 1
m2 = 2
r2 = 3
d1 = 4
r1 = 5
r3 = 6
d2 = 7
rccw = r3
rcw = r1

def reversal(x):
    y = 0
    for i in range(10):
        y <<= 1;
        if x&1:
            y |= 1
        x >>= 1
    return y

# this gets a number generated from the top side after transform
def getnum(g,tile):
    f = xfrm[g]
    n = 0
    for x,y in map(f, range(10), itertools.repeat(0,10)):
        n <<= 1
        if tile[y][x]:
            n |= 1
    return n


border1 = frozenset([101, 107, 110, 118, 139, 145, 148, 174, 19, 190, 2, 205, 213, 22, 24, 243, 25, 26, 271, 273, 309, 310, 33, 337, 346, 371, 439, 445, 489, 49, 535, 539, 559, 567, 573, 587, 595, 619, 621, 623, 631, 723, 747, 75, 751, 795, 855, 919])

border = frozenset(itertools.chain(border1, (reversal(i) for i in border1)))

edgemap = {}

inf = sys.stdin
for i in range(144):
    inf.readline()
    tile = []
    for j in range(10):
        tile.append([])
        line = inf.readline().rstrip()
        for k in range(10):
            tile[j].append(1 if line[k] == '#' else 0)
    for j in range(8):
        k = getnum(j, tile)
        edgemap.setdefault(k, []).append((j, tile))
    inf.readline()

resmap = []
resmap.append([edgemap[554][0]])

def printtile(t):
    f = xfrm[t[0]]
    for j in range(10):
        for l in range(10):
            x,y = f(l,j)
            sys.stdout.write('#' if t[1][y][x] else '.')
        print()
    print()
def select_other(tt, t):
    return tt[1] if tt[0][1] == t[1] else tt[0]

rotate_flip = comp[m1][r2]
for i in range(1,12):
    t = resmap[i-1][0]
    n = getnum(comp[rotate_flip][t[0]], t[1])
    t2 = select_other(edgemap[n], t);
    resmap.append([t2])

rotate_flip2 = comp[m1][rccw]
for i in range(12):
    for j in range(1,12):
        t = resmap[i][j-1]
        n = getnum(comp[rotate_flip2][t[0]], t[1])
        t2 = select_other(edgemap[n], t)
        resmap[i].append((comp[rccw][t2[0]], t2[1]))

for i in range(12):
    for j in range(1,9):
        for k in range(12):
            t = resmap[i][k]
            f = xfrm[t[0]]
            for l in range(1,9):
                x,y = f(l,j)
                sys.stdout.write('#' if t[1][y][x] else '.')
        print()



