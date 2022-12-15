#!/usr/bin/env python3
excluded = set()
try:
    while True:
        line = input().split()
        sx, sy, bx, by = map(int, (line[2][2:-1], line[3][2:-1], line[8][2:-1], line[9][2:]))
        maxmd = abs(sx-bx)+abs(sy-by)
        md2m = abs(sy-2000000)
        if md2m <= maxmd:
            for i in range(sx-(maxmd-md2m), sx+(maxmd-md2m)):
                excluded.add(i)
except EOFError:
    pass
print(len(excluded))
