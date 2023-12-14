#!/usr/bin/env python3
import sys
m = [[ch for ch in line.rstrip()] for line in sys.stdin]
for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch == 'O':
            y2 = y
            while y2 and m[y2-1][x] == '.':
                y2 -= 1
            if y != y2:
                m[y2][x] = 'O'
                m[y][x] = '.'

print(sum((len(m)-y)*line.count('O') for y, line in enumerate(m)))
