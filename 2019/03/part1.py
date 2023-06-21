#!/usr/bin/env python3
def makeset(line):
    s = set()
    x, y = 0, 0
    for step in line.split(','):
        if step[0] == 'R':
            dx, dy = 1, 0
        elif step[0] == 'U':
            dx, dy = 0, 1
        elif step[0] == 'L':
            dx, dy = -1, 0
        elif step[0] == 'D':
            dx, dy = 0, -1
        for i in range(int(step[1:])):
            x += dx
            y += dy
            s.add((x, y))
    return s
a = makeset(input())
b = makeset(input())
print(min(abs(x)+abs(y) for x, y in a.intersection(b)))
