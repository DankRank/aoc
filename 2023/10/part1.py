#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
tab = {
    '|': (1, 3),
    '-': (0, 2),
    'L': (0, 1),
    'J': (1, 2),
    '7': (2, 3),
    'F': (0, 3),
}
def check(x, y, d):
    count = 0
    while True:
        count += 1
        if y < 0 or y >= len(m) or x < 0 or x >= len(m[0]):
            return None
        ch = m[y][x]
        if ch in tab:
            if d == tab[ch][0]^2:
                d = tab[ch][1]
            elif d == tab[ch][1]^2:
                d = tab[ch][0]
            else:
                return None
            x += dirs[d][0]
            y += dirs[d][1]
        elif ch == 'S':
            return count
        else:
            return None

sx, sy = [(x, y) for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'S'][0]
for i in range(4):
    res = check(sx+dirs[i][0], sy+dirs[i][1], i)
    if res is not None:
        break
print(res//2)
