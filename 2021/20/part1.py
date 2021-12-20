#!/usr/bin/env python3
algomap = list(map(lambda x: x == '#', input()))
input()

image = []
try:
    while True:
        image.append(list(input()))
except EOFError:
    pass

def enchance(imgset, minbound, maxbound, outofrange):
    def check(x,y,val):
        if x < minbound or x > maxbound or y < minbound or y > maxbound:
            return val if outofrange else 0
        else:
            return val if (x,y) in imgset else 0
    newset = set()
    for i in range(minbound-1, maxbound+2):
        for j in range(minbound-1, maxbound+2):
            if algomap[
                check(i-1, j-1, 256) +
                check(i-1, j,   128) +
                check(i-1, j+1, 64) +
                check(i,   j-1, 32) +
                check(i,   j,   16) +
                check(i,   j+1, 8) +
                check(i+1, j-1, 4) +
                check(i+1, j,   2) +
                check(i+1, j+1, 1)]:
                newset.add((i, j))
    return newset, minbound-1, maxbound+1, algomap[511 if outofrange else 0]

imgset = {(i, j) for i in range(len(image)) for j in range(len(image[0])) if image[i][j] == '#'}
minbound = 0
maxbound = len(image)-1
outofrange = False
for i in range(2):
    imgset, minbound, maxbound, outofrange = enchance(imgset, minbound, maxbound, outofrange)
print(len(imgset))
