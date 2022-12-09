#!/usr/bin/env python3
scr = [[0]*50 for i in range(6)]
try:
    while True:
        line = input().split()
        if line[0] == 'rect':
            x, y = map(int, line[1].split('x'))
            for i in range(y):
                for j in range(x):
                    scr[i][j] = 1
        elif line[1] == 'row':
            r = int(line[2][2:])
            by = int(line[4]) % 50
            scr[r] = scr[r][-by:] + scr[r][:-by]
        elif line[1] == 'column':
            c = int(line[2][2:])
            by = int(line[4]) % 6
            for i in range(by):
                scr[0][c], scr[1][c], scr[2][c], scr[3][c], scr[4][c], scr[5][c] = scr[5][c], scr[0][c], scr[1][c], scr[2][c], scr[3][c], scr[4][c]
except EOFError:
    pass
print('\n'.join(''.join(map(lambda x: '#' if x == 1 else ' ', s)) for s in scr))
