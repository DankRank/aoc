#!/usr/bin/env python3
m = []
movelist = []
try:
    line = input()
    while line != '':
        m.append(list(line))
        line = input()
    while True:
        movelist.append(input())
except EOFError:
    pass

movelist = ''.join(movelist)
for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch == '@':
            line[x] = '.'
            startpos = (x, y)
todir = { '^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0) }

px, py = startpos
for move in movelist:
    dx, dy = todir[move]
    x, y = px+dx, py+dy
    while m[y][x] != '#':
        if m[y][x] == '.':
            px += dx
            py += dy
            if px != x or py != y:
                m[y][x] = 'O'
                m[py][px] = '.'
            break
        x += dx
        y += dy
print(sum(y*100 + x for y, line in enumerate(m) for x, ch in enumerate(line) if ch == 'O'))
