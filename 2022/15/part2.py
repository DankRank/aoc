#!/usr/bin/env pypy3
sensors = []
ranges = [[] for i in range(4000001)]
try:
    while True:
        line = input().split()
        sx, sy, bx, by = map(int, (line[2][2:-1], line[3][2:-1], line[8][2:-1], line[9][2:]))
        sensors.append((sx, sy, bx, by))
except EOFError:
    pass
for sx, sy, bx, by in sensors:
    maxmd = abs(sx-bx)+abs(sy-by)
    for y in range(0, 4000001):
        d = maxmd-abs(y-sy)
        if d >= 0:
            ranges[y].append((sx-d, sx+d+1))
def range_merger(rs):
    i = 1
    j = 0
    while i < len(rs):
        if rs[j][1] >= rs[i][0]:
            rs[j] = (rs[j][0], max(rs[j][1], rs[i][1]))
            del rs[i]
        else:
            j = i
            i += 1
def range_clamper(rs):
    i = 0
    while i < len(rs):
        if rs[i][0] < 0 or rs[i][1] > 4000001:
            rs[i] = (max(rs[i][0], 0), min(rs[i][1], 4000001))
            if rs[i][0] == rs[i][1]:
                del rs[i]
                i -= 1
        i += 1
for y, rs in enumerate(ranges):
    rs.sort()
    range_merger(rs)
    range_clamper(rs)
    if len(rs) > 1:
        print(rs[0][1]*4000000 + y)
        break
