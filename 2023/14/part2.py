#!/usr/bin/env python3
import sys
import functools
m = [[ch for ch in line.rstrip()] for line in sys.stdin]
h = len(m)
w = len(m[0])
def spin(m):
    m = [list(line) for line in m]
    # north
    for y in range(h):
        for x in range(w):
            if m[y][x] == 'O':
                y2 = y
                while y2 and m[y2-1][x] == '.':
                    y2 -= 1
                if y != y2:
                    m[y2][x] = 'O'
                    m[y][x] = '.'
    # west
    for y in range(h):
        for x in range(w):
            if m[y][x] == 'O':
                x2 = x
                while x2 and m[y][x2-1] == '.':
                    x2 -= 1
                if x != x2:
                        m[y][x2] = 'O'
                        m[y][x] = '.'
    # south
    for y in range(h-1, -1, -1):
        for x in range(w):
            if m[y][x] == 'O':
                y2 = y
                while y2<h-1 and m[y2+1][x] == '.':
                    y2 += 1
                if y != y2:
                    m[y2][x] = 'O'
                    m[y][x] = '.'
    # east
    for y in range(h):
        for x in range(w-1, -1, -1):
            if m[y][x] == 'O':
                x2 = x
                while x2<w-1 and m[y][x2+1] == '.':
                    x2 += 1
                if x != x2:
                        m[y][x2] = 'O'
                        m[y][x] = '.'
    return tuple(tuple(line) for line in m)

m = tuple(tuple(line) for line in m)
seen = {m: 0}
seenls = [m]
i = 0
while True:
    m = spin(m)
    i += 1
    if m not in seen:
        seen[m] = i
        seenls.append(m)
    else:
        break
m = seenls[seen[m] + (1000000000-i)%(i - seen[m])]
print(sum((len(m)-y)*line.count('O') for y, line in enumerate(m)))
