#!/usr/bin/env python3
def sign(x):
    return (x > 0) - (x < 0)
visited = {(0, 0)}
rx = [0]*10
ry = [0]*10
def sym(h, t):
    if abs(rx[h]-rx[t]) > 1 or abs(ry[h]-ry[t]) > 1:
        rx[t] += sign(rx[h]-rx[t])
        ry[t] += sign(ry[h]-ry[t])
try:
    while True:
        d, l = input().split()
        dx, dy = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}[d]
        for i in range(int(l)):
            rx[0] += dx
            ry[0] += dy
            for i in range(9):
                sym(i, i+1)
            visited.add((rx[9], ry[9]))
except EOFError:
    pass
print(len(visited))
