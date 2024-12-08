#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
w, h = len(m[0]), len(m)

antennae = {}
for y, line in enumerate(m):
    for x, ch in enumerate(line):
        if ch != '.':
            if ch in antennae:
                antennae[ch].append((x, y))
            else:
                antennae[ch] = [(x, y)]
antinodes = set()

for ls in antennae.values():
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j:
                (x1, y1), (x2, y2) = ls[i], ls[j]
                x3, y3 = x2 + (x2-x1), y2 + (y2-y1)
                if 0 <= x3 < w and 0 <= y3 < h:
                    antinodes.add((x3, y3))
print(len(antinodes))
