#!/usr/bin/env python3
potential = set()
sensors = []
def gen_bounded_points(sx, sy, d):
    # +x -y
    i, x, y = 0, sx-maxmd, sy
    if x < 0:
        i += 0-x
        y -= 0-x
        x = 0
    if y > 4000000:
        i += y-4000000
        x += y-4000000
        y = 4000000
    while i < d and x <= 4000000 and y >= 0:
        yield x, y
        x += 1
        y -= 1
        i += 1
    # +x +y
    i, x, y = 0, sx, sy-maxmd
    if y < 0:
        i += 0-y
        x += 0-y
        y = 0
    if x < 0:
        i += 0-x
        y += 0-x
        x = 0
    while i < d and x <= 4000000 and y <= 4000000:
        yield x, y
        x += 1
        y += 1
        i += 1
    # -x +y
    i, x, y = 0, sx+maxmd, sy
    if x > 4000000:
        i += x-4000000
        y += x-4000000
        x = 4000000
    if y < 0:
        i += 0-y
        x -= 0-y
        y = 0
    while i < d and x <= 4000000 and y >= 0:
        yield x, y
        x -= 1
        y += 1
        i += 1
    # -x -y
    i, x, y = 0, sx, sy+maxmd
    if y > 4000000:
        i += y-4000000
        x -= y-4000000
        y = 4000000
    if x > 4000000:
        i += x-4000000
        y -= x-4000000
        x = 4000000
    while i < d and x >= 0 and y >= 0:
        yield x, y
        x -= 1
        y -= 1
        i += 1


try:
    while True:
        line = input().split()
        sx, sy, bx, by = map(int, (line[2][2:-1], line[3][2:-1], line[8][2:-1], line[9][2:]))
        sensors.append((sx, sy, bx, by))
except EOFError:
    pass
for sx, sy, bx, by in sensors:
    maxmd = abs(sx-bx)+abs(sy-by)
    print('tick', len(potential))
    for x, y in gen_bounded_points(sx, sy, maxmd+1):
        potential.add((x, y))
print(len(potential))
