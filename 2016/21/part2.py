#!/usr/bin/env python3
import sys
pwd = list('fbgdceah')
mapp = {1:0, 3:1, 5:2, 7:3, 2:4, 4:5, 6:6, 0:7}
lines = sys.stdin.read().splitlines()
for line in lines[::-1]:
    line = line.split()
    if line[0] == 'swap':
        if line[1] == 'letter':
            a = pwd.index(line[2])
            b = pwd.index(line[5])
        else:
            assert line[1] == 'position'
            a = int(line[2])
            b = int(line[5])
        pwd[a], pwd[b] = pwd[b], pwd[a]
    elif line[0] == 'rotate':
        if line[1] == 'left':
            a = -int(line[2]) % len(pwd)
        elif line[1] == 'right':
            a = int(line[2]) % len(pwd)
        else:
            assert line[1] == 'based'
            a = mapp[pwd.index(line[6])]
            a += 2 if a >= 4 else 1
            a = a % len(pwd)
        pwd = pwd[a:]+pwd[:a]
    elif line[0] == 'reverse':
        a = int(line[2])
        b = int(line[4])
        pwd[a:b+1] = pwd[b:a-1-len(pwd):-1]
    else:
        assert line[0] == 'move'
        b = int(line[2])
        a = int(line[5])
        c = pwd[a]
        del pwd[a]
        pwd[b:b] = c
print(''.join(pwd))
