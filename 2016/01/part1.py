#!/usr/bin/env python3
steps = input().split(', ')
x, y = 0, 0
dx, dy = 0, 1
for step in steps:
    if step[0] == 'L':
        dx, dy = -dy, dx
    else:
        dx, dy = dy, -dx
    d = int(step[1:])
    x += dx * d
    y += dy * d
print(abs(x)+abs(y))
