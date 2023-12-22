#!/usr/bin/env python3
import sys
m = [[[int(c) for c in endpoint.split(',')] for endpoint in line.rstrip().split('~')]  for line in sys.stdin ]
blockmap = {}
for bi, b in enumerate(m):
    assert b[0][0] <= b[1][0] and b[0][1] <= b[1][1] and b[0][2] <= b[1][2]
    for i in range(b[0][0], b[1][0]+1):
        for j in range(b[0][1], b[1][1]+1):
            for k in range(b[0][2], b[1][2]+1):
                blockmap[i, j, k] = bi
def canmovedown(b):
    k = b[0][2]-1
    if k == 0:
        return False
    for i in range(b[0][0], b[1][0]+1):
        for j in range(b[0][1], b[1][1]+1):
            if (i, j, k) in blockmap:
                return False
    return True
def findallxyplane(b, k):
    ls = set()
    for i in range(b[0][0], b[1][0]+1):
        for j in range(b[0][1], b[1][1]+1):
            if (i, j, k) in blockmap:
                ls.add(blockmap[i, j, k])
    return ls
def findallbelow(b):
    return findallxyplane(b, b[0][2]-1)
def findallabove(b):
    return findallxyplane(b, b[1][2]+1)

stable = False
while not stable:
    stable = True
    for bi, b in enumerate(m):
        movedby = 0
        while canmovedown(b):
            movedby += 1
            b[0][2] -= 1
            b[1][2] -= 1
        if movedby:
            h = min(movedby, b[1][2]+1-b[0][2])
            for i in range(b[0][0], b[1][0]+1):
                for j in range(b[0][1], b[1][1]+1):
                    for k in range(b[1][2]+1+movedby-h, b[1][2]+1+movedby):
                        del blockmap[i, j, k]
                    for k in range(b[0][2], b[0][2]+h):
                        blockmap[i, j, k] = bi
            stable = False

allabove = {}
allbelow = {}
for bi, b in enumerate(m):
    allabove[bi] = findallabove(b)
    allbelow[bi] = findallbelow(b)

count = 0
for bi, b in enumerate(m):
    if all(len(allbelow[bi2]) > 1 for bi2 in allabove[bi]):
        count += 1
print(count)

count = 0
for bi, b in enumerate(m):
    chain = 0
    removed = {bi}
    tocheck = allabove[bi].copy()
    while len(tocheck):
        bi2 = tocheck.pop()
        assert bi2 not in removed
        if allbelow[bi2] <= removed:
            chain += 1
            removed.add(bi2)
            tocheck |= allabove[bi2]
    count += chain
print(count)
