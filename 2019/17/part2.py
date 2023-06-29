#!/usr/bin/env python3
from intcode import *
vm = IntcodeVM(parsetext(input()))
vm.text[0] = 2
vm.run()
m = ['.'+x+'.' for x in ''.join(chr(x) for x in vm.outq).split()]
del m[-1]
m.insert(0, '.'*len(m[0]))
m.append('.'*len(m[0]))
scaffolds = set()
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] not in '.#':
            if m[i][j] == '^':
                dx, dy = 0, -1
            elif m[i][j] == 'V':
                dx, dy = 0, 1
            elif m[i][j] == '<':
                dx, dy = -1, 0
            elif m[i][j] == '>':
                dx, dy = 1, 0
            else:
                raise ValueError(f'what\'s {m[i][j]}')
            x, y = j, i
        if m[i][j] != '.':
            scaffolds.add((j, i))
path = []
fwd = 0
while True:
    while (x+dx, y+dy) in scaffolds:
        x += dx
        y += dy
        fwd += 1
    if fwd:
        path.append(str(fwd))
        fwd = 0
    # turn left: y, -x
    # turn right: -y, x
    if (x+dy, y-dx) in scaffolds:
        path.append('L')
        dx, dy = dy, -dx
    elif (x-dy, y+dx) in scaffolds:
        path.append('R')
        dx, dy = -dy, dx
    else:
        break
progs = []
main = []
# educated guess
for i in [8, 8, 8, 6, 8, 8, 6, 8, 6, 8]:
    # print(path[:i])
    try:
        idx = progs.index(path[:i])
    except ValueError:
        idx = len(progs)
        progs.append(path[:i])
    main.append(chr(65+idx))
    path = path[i:]
vm.outq = []
vm.inq += ''.join(','.join(line)+'\n' for line in [main, *progs, ['n']]).encode()
vm.run()
print(vm.outq[-1])
