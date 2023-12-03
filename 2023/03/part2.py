#!/usr/bin/env python3
import sys
lines = [line.rstrip() for line in sys.stdin]
m = {(r,c): ch for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == '*'}
h = len(lines)
w = len(lines[0])
def neighbors(i, j, k):
    yield (i, j-1)
    yield (i, k)
    for x in range(j-1, k+1):
        yield (i-1, x)
        yield (i+1, x)
adj = {}
for i, line in enumerate(lines):
    j = 0
    while j < w:
        if not line[j].isdigit():
            j += 1
            continue
        k = j+1
        while k < w and line[k].isdigit():
            k += 1
        for n in neighbors(i, j, k):
            if n in m:
                if n not in adj:
                    adj[n] = [int(line[j:k])]
                else:
                    adj[n].append(int(line[j:k]))
        j = k+1
s = 0
for n, ls in adj.items():
    if len(ls) == 2:
        s += ls[0]*ls[1]
print(s)
