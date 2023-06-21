#!/usr/bin/env python3
W, H = 25, 6
p = input()
for y in range(H):
    line = []
    for x in range(W):
        i = y*W+x
        while p[i] == '2':
            i += W*H
        line.append('#' if p[i] == '1' else ' ')
    print(''.join(line))
