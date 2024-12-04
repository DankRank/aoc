#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)
vecs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
count = 0
for i in range(h):
    for j in range(w):
        if m[i][j] == 'X':
            for dy, dx in vecs:
                if 0 <= i+dy*3 < h and 0 <= j+dx*3 < w:
                    if ''.join(m[i+dy*k][j+dx*k] for k in range(1, 4)) == 'MAS':
                        count += 1
print(count)
