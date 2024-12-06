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

visited = {(x,y)}
while 0 <= x+dx < w and 0 <= y+dy < h:
    while m[y+dy][x+dx] == '#':
        dx, dy = -dy, dx
    x += dx
    y += dy
    visited.add((x, y))
print(len(visited))
