#!/usr/bin/env python3
def sign(x):
    return (x > 0) - (x < 0)
visited = {(0, 0)}
hx, hy, tx, ty = 0, 0, 0, 0
try:
    while True:
        d, l = input().split()
        dx, dy = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}[d]
        for i in range(int(l)):
            hx += dx
            hy += dy
            if abs(hx-tx) > 1 or abs(hy-ty) > 1:
                tx += sign(hx-tx)
                ty += sign(hy-ty)
                visited.add((tx, ty))
except EOFError:
    pass
print(len(visited))
