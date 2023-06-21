#!/usr/bin/env python3
W, H = 25, 6
p = input()
minzeroes = float('inf')
res = None
for i in range(0, len(p), W*H):
    layer = p[i:i+W*H]
    zeroes = layer.count('0')
    if zeroes < minzeroes:
        minzeroes = zeroes
        res = layer.count('1')*layer.count('2')
print(res)
