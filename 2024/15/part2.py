#!/usr/bin/env python3
m = []
movelist = []

def remapline(line):
    nline = []
    for ch in line:
        if ch == 'O':
            nline += '[]'
        elif ch == '@':
            nline += '@.'
        else:
            nline += ch*2
    return nline

try:
    line = input()
    while line != '':
        m.append(remapline(line))
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

def canmoveboxat(x, y, dy):
    if m[y][x] == ']':
        x -= 1
    if m[y+dy][x] == '#' or m[y+dy][x+1] == '#':
        return False
    canmove = True
    if m[y+dy][x] in '[]':
        canmove = canmoveboxat(x, y+dy, dy)
    if m[y+dy][x+1] == '[':
        canmove = canmove and canmoveboxat(x+1, y+dy, dy)
    return canmove
def moveboxat(x, y, dy):
    if m[y][x] == ']':
        x -= 1
    if m[y+dy][x] in '[]':
        moveboxat(x, y+dy, dy)
    if m[y+dy][x+1] == '[':
        moveboxat(x+1, y+dy, dy)
    m[y+dy][x] = '['
    m[y+dy][x+1] = ']'
    m[y][x] = '.'
    m[y][x+1] = '.'

def trypush(px, py, dx, dy):
    if dx:
        x = px+dx
        while m[py][x] != '#':
            if m[py][x] == '.':
                last = '.'
                for i in range(px+dx, x+dx, dx):
                    last, m[py][i] = m[py][i], last
                return px+dx, py
            x += dx
        return px, py
    else:
        if m[py+dy][px] != '#':
            if m[py+dy][px] == '.':
                return px, py+dy
            if canmoveboxat(px, py+dy, dy):
                moveboxat(px, py+dy, dy)
                return px, py+dy
    return px, py

for move in movelist:
    dx, dy = todir[move]
    px, py = trypush(px, py, dx, dy)
print(sum(y*100 + x for y, line in enumerate(m) for x, ch in enumerate(line) if ch == '['))
