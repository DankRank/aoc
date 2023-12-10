#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
tab = {
    '|': (1, 3),
    '-': (0, 2),
    'L': (0, 1),
    'J': (1, 2),
    '7': (2, 3),
    'F': (0, 3),
}
def check(x, y, d):
    initd = d
    pipes = set()
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
    while True:
        pipes.add((x, y))
        if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
            return None, None
        ch = m[y][x]
        if ch in tab:
            lastd = d
            if d == tab[ch][0]^2:
                d = tab[ch][1]
            elif d == tab[ch][1]^2:
                d = tab[ch][0]
            else:
                return None, None
            addadj(x, y, lastd, d)
            x += dirs[d][0]
            y += dirs[d][1]
        elif ch == 'S':
            addadj(x, y, d, initd)
            return pipes, adj
        else:
            return None, None

sx, sy = [(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'S'][0]
for i in range(4):
    res, adj = check(sx+dirs[i][0], sy+dirs[i][1], i)
    if res is not None:
        break

count = 0
for y in range(len(m)):
    winding = 0
    for x in range(len(m[0])):
        if (x, y) in adj:
            winding += adj[x, y]
        elif winding and (x, y) not in res:
            count += 1
print(count)
