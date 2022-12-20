#!/usr/bin/env python3
import sys
ls = [[int(line), i] for i, line in enumerate(sys.stdin.read().splitlines())]
lsi = [s for s in ls]
for i in lsi:
    src = ls.index(i)
    dst = (src + i[0] - 1)%(len(ls)-1) + 1
    del ls[src:src+1]
    ls[dst:dst] = [i]
for i,j in enumerate(ls):
    if j[0] == 0:
        print(sum(ls[(i+k)%len(ls)][0] for k in (1000, 2000, 3000)))
        break


