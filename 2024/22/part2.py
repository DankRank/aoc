#!/usr/bin/env python3
import sys
m = [int(line.rstrip()) for line in sys.stdin]

def nextnum(i):
    i = (i^(i<<6)) & 0xffffff
    i = (i^(i>>5)) & 0xffffff
    i = (i^(i<<11)) & 0xffffff
    return i

gmap = {}
for s in m:
    ls = [s%10]
    for i in range(2000):
        s = nextnum(s)
        ls.append(s%10)
    dls = [ls[i+1]-ls[i] for i in range(len(ls)-1)]
    tls = [tuple(dls[i:i+4]) for i in range(len(dls)-3)]
    tmap = {}
    for i, t in enumerate(tls):
        if t not in tmap:
            tmap[t] = ls[i+4]
    for i, v in tmap.items():
        if i not in gmap:
            gmap[i] = v
        else:
            gmap[i] += v
print(max(gmap.values()))
