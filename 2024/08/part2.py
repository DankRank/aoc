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
                dx, dy = x2-x1, y2-y1
                while 0 <= x2 < w and 0 <= y2 < h:
                    antinodes.add((x2, y2))
                    x2, y2 = x2 + dx, y2 + dy
print(len(antinodes))
