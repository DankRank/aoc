#!/usr/bin/env python3
import sys
m = {(x, y) for y, line in enumerate(sys.stdin) for x, ch in enumerate(line.rstrip()) if ch == '#'}
maxx = max(m, key=lambda x: x[0])[0]+1
maxy = max(m, key=lambda x: x[1])[1]+1
xcosts = [1000000 if not any(x == i for x, y in m) else 1 for i in range(maxx)]
ycosts = [1000000 if not any(y == i for x, y in m) else 1 for i in range(maxy)]
s = 0
m = list(m)
for i in range(len(m)):
    for j in range(i+1, len(m)): 
        minx = min(m[i][0], m[j][0])
        maxx = max(m[i][0], m[j][0])
        miny = min(m[i][1], m[j][1])
        maxy = max(m[i][1], m[j][1])
        s += sum(xcosts[i] for i in range(minx, maxx+1))-1
        s += sum(ycosts[i] for i in range(miny, maxy+1))-1
print(s)
