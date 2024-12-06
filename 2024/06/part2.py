#!/usr/bin/env python3
import functools
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

def nextstep(x, y, dx, dy, nx, ny):
    while 0 <= x+dx < w and 0 <= y+dy < h and m[y+dy][x+dx] != '#' and (x+dx, y+dy) != (nx, ny):
        x += dx
        y += dy
    if not (0 <= x+dx < w and 0 <= y+dy < h):
        return x+dx, y+dy, 0, 0
    return x, y, -dy, dx
nextstepcache = functools.cache(nextstep)
def checkobs(x, y, dx, dy, nx, ny):
    visited = {(x, y, dx, dy)}
    while 0 <= x+dx < w and 0 <= y+dy < h:
        if x != nx and y != ny:
            x, y, dx, dy = nextstepcache(x, y, dx, dy, None, None)
        else:
            x, y, dx, dy = nextstep(x, y, dx, dy, nx, ny)
        if (x, y, dx, dy) in visited:
            return True
        visited.add((x, y, dx, dy))
    return False
print(sum(int(checkobs(x,y,dx,dy,nx,ny)) for ny, line in enumerate(m) for nx, ch in enumerate(line) if ch == '.'))
