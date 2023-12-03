#!/usr/bin/env python3
import sys
lines = [line.rstrip() for line in sys.stdin]
m = {(r,c): ch for r, line in enumerate(lines) for c, ch in enumerate(line) if ch != '.' and not ch.isdigit()}
h = len(lines)
w = len(lines[0])
def neighbors(i, j, k):
    yield (i, j-1)
    yield (i, k)
    for x in range(j-1, k+1):
        yield (i-1, x)
        yield (i+1, x)
s = 0
for i, line in enumerate(lines):
    j = 0
    while j < w:
        if not line[j].isdigit():
            j += 1
            continue
        k = j+1
        while k < w and line[k].isdigit():
            k += 1
        if any(n in m for n in neighbors(i, j, k)):
            s += int(line[j:k])
        j = k+1
print(s)
