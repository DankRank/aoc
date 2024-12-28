#!/usr/bin/env python3
import sys
claims = []
for line in sys.stdin:
    line = line.rstrip()
    a, b = line.split(' @ ')
    c, d = b.split(': ')
    id = a.removeprefix('#')
    x, y = (int(i) for i in c.split(','))
    w, h = (int(i) for i in d.split('x'))
    claims.append((id, x, y, w, h))

m = [[0]*1000 for i in range(1000)]
for id, x, y, w, h in claims:
    for i in range(y, y+h):
        for j in range(x, x+w):
            m[i][j] += 1
print(sum(int(x > 1) for line in m for x in line))

def find():
    for id, x, y, w, h in claims:
        for i in range(y, y+h):
            for j in range(x, x+w):
                if m[i][j] > 1:
                    break
            else:
                continue
            break
        else:
            return id
print(find())
