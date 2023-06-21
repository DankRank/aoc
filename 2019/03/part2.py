#!/usr/bin/env python3
def makeset(line):
    s = {}
    d = 0
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
            d += 1
            if (x, y) not in s:
                s[(x, y)] = d
    return s
a = makeset(input())
b = makeset(input())
print(min(a[p]+b[p] for p in set(a.keys()).intersection(set(b.keys()))))
