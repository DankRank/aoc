#!/usr/bin/env python3
from itertools import chain
field = [[0 for i in range(1000)] for i in range(1000)]
try:
    while True:
        src,dst = input().split(' -> ')
        x1,y1 = map(int, src.split(','))
        x2,y2 = map(int, dst.split(','))
        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                field[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                field[y1][i] += 1
except EOFError:
    pass
print(sum(1 for i in filter(lambda x: x > 1, chain(*field))))
