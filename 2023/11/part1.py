#!/usr/bin/env python3
import sys
m = {(x, y) for y, line in enumerate(sys.stdin) for x, ch in enumerate(line.rstrip()) if ch == '#'}
# very inefficient implementation of the expansion
maxx = max(m, key=lambda x: x[0])[0]
maxy = max(m, key=lambda x: x[1])[1]
i = 0
while i < maxx:
    if not any(x == i for x, y in m):
        m = {(x+int(x>=i), y) for x, y in m}
        i += 1
        maxx += 1
    i += 1
i = 0
while i < maxy:
    if not any(y == i for x, y in m):
        m = {(x, y+int(y>=i)) for x, y in m}
        i += 1
        maxy += 1
    i += 1
# shortest paths
s = 0
m = list(m)
for i in range(len(m)):
    for j in range(i+1, len(m)): 
        s += abs(m[i][0]-m[j][0]) + abs(m[i][1]-m[j][1])
print(s)
