#!/usr/bin/env python3
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dmap = {'R':0, 'U':1, 'L':2, 'D':3}
firstd = None
lastd = None
pts = set()
adj = {}
def addadj(x, y, frm, to):
    if frm == 1 and to == 1:
        adj[x, y] = 2
    elif frm == 1 or to == 1:
        adj[x, y] = 1
    elif frm == 3 and to == 3:
        adj[x, y] = -2
    elif frm == 3 or to == 3:
        adj[x, y] = -1
x, y = 0, 0
try:
    while True:
        d, r, c = input().split()
        d, r = dmap[d], int(r)
        if lastd is not None:
            addadj(x, y, lastd, d)
            lastd = d
        else:
            lastd = firstd = d
        for i in range(r):
            x += dirs[d][0]
            y += dirs[d][1]
            pts.add((x, y))
            if i != r-1:
                addadj(x, y, d, d)
except EOFError:
    pass

assert x == 0 and y == 0
addadj(0, 0, lastd, firstd)
minx = min(pts, key=lambda x: x[0])[0]
maxx = max(pts, key=lambda x: x[0])[0]
miny = min(pts, key=lambda x: x[1])[1]
maxy = max(pts, key=lambda x: x[1])[1]
count = 0
for y in range(miny, maxy+1):
    winding = 0
    for x in range(minx, maxx+1):
        if (x, y) in adj:
            winding += adj[x, y]
        if winding or (x, y) in pts:
            count += 1
print(count)
