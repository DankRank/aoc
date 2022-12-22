#!/usr/bin/env python3
import re
mapp = []
xfix = []
yfix = []
while True:
    line = input()
    if line == '':
        break
    mapp.append(line)
    pos = re.search('[.#]', line).span()[0]
    xfix.append((pos, len(line)-pos))

maxw = max(len(x) for x in mapp)
for i,v in enumerate(mapp):
    if maxw > len(v):
        mapp[i] += (maxw - len(v))*' '

# transpose
mapq = [''.join(mapp[y][x] for y in range(len(mapp))) for x in range(len(mapp[0]))]
for line in mapq:
    pos = re.search('[.#]', line).span()[0]
    yfix.append((pos, len(line.rstrip())-pos))

cmds = re.sub('[LR]', r' \g<0> ', input()).split()
dx, dy = 1, 0
di = 0
x = re.search('[.#]', mapp[0]).span()[0]
y = 0
for cmd in cmds:
    if cmd == 'R':
        dx, dy, di = -dy, dx, di+1
    elif cmd == 'L':
        dx, dy, di = dy, -dx, di-1
    else:
        for i in range(int(cmd)):
            if dx != 0:
                p, q = xfix[y]
                nx, ny = (x+dx - p)%q + p, y
            else:
                p, q = yfix[x]
                nx, ny = x, (y+dy - p)%q + p
            if mapp[ny][nx] == '.':
                x, y = nx, ny
print((y+1)*1000 + (x+1)*4 + di%4)
