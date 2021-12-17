#!/usr/bin/env python3
_, _, xstr, ystr = input().split()
minx, maxx = map(int, xstr[2:-1].split('..'))
miny, maxy = map(int, ystr[2:].split('..'))
def check(vx0, vy0):
    x = 0
    y = 0
    vx = vx0
    vy = vy0
    while True:
        if (y < miny and vy < 0) or (x < minx and vx <= 0) or (x > maxx and vx >= 0):
            return False
        if minx <= x and x <= maxx and miny <= y and y <= maxy:
            return True
        x += vx
        y += vy
        if vx != 0:
            vx -= 1 if vx > 0 else -1
        vy -= 1
# wow this is really terrible
#for i in range(-200, 200):
#    print(''.join('#' if check(i,j) else '.' for j in range(-200, 200)))
print(sum(1 for i in range(-200, 200) for j in range(-200, 200) if check(i, j)))
