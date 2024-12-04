#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)
vecs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
count = 0
for i in range(h):
    for j in range(w):
        if m[i][j] == 'M':
            for dy, dx in vecs:
                if 0 <= i+dy*2 < h and 0 <= j+dx*2 < w:
                    if ''.join(m[i+dy*k][j+dx*k] for k in range(1,3)) == 'AS':
                        if m[i+dy+dy][j] + m[i][j+dx+dx] in ('MS', 'SM'):
                            count += 1
print(count//2)
