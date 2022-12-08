#!/usr/bin/env python3
import sys
steps = input().split(', ')
x, y = 0, 0
dx, dy = 0, 1
visited = {(0, 0)}
for step in steps:
    if step[0] == 'L':
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    d = int(step[1:])
    for i in range(d):
        x += dx
        y += dy
        if (x, y) in visited:
            print(abs(x)+abs(y))
            sys.exit(0)
        visited.add((x, y))
