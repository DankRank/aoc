#!/usr/bin/env python3
s = 0
try:
    while True:
        line = input().split(': ')[1]
        maxcubes = {'red':0, 'green':0, 'blue':0}
        for bagset in line.split('; '):
            for cubes in bagset.split(', '):
                cnt, col = cubes.split(' ')
                cnt = int(cnt)
                if maxcubes[col] < cnt:
                    maxcubes[col] = cnt
        s += maxcubes['red']*maxcubes['green']*maxcubes['blue']
except EOFError:
    pass
print(s)
