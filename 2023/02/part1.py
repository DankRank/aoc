#!/usr/bin/env python3
maxred = 12
maxgreen = 13
maxblue = 14
gameno = 1
s = 0
try:
    while True:
        line = input().split(': ')[1]
        for bagset in line.split('; '):
            for cubes in bagset.split(', '):
                cnt, col = cubes.split(' ')
                cnt = int(cnt)
                if col == 'red':
                    if cnt > maxred:
                        break
                elif col == 'green':
                    if cnt > maxgreen:
                        break
                elif col == 'blue':
                    if cnt > maxblue:
                        break
            else:
                continue
            break
        else:
            s += gameno
        gameno += 1
except EOFError:
    pass
print(s)
