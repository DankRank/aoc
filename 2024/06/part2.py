#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)
for y, line in enumerate(m):
    x = line.find('^')
    if x != -1:
        break
else:
    raise ValueError('start pos not found')
dx, dy = 0, -1

def checkobs(x, y, dx, dy, nx, ny):
    visited = {(x, y, dx, dy)}
    while 0 <= x+dx < w and 0 <= y+dy < h:
        while m[y+dy][x+dx] == '#' or x+dx == nx and y+dy == ny:
            dx, dy = -dy, dx
        x += dx
        y += dy
        if (x, y, dx, dy) in visited:
            return True
        visited.add((x, y, dx, dy))
    return False
print(sum(int(checkobs(x,y,dx,dy,nx,ny)) for ny, line in enumerate(m) for nx, ch in enumerate(line) if ch == '.'))
