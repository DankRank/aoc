#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0
st = [(0, 0, 0)]
seen = set()
seenspot = set()
def advance(x, y, d):
    x += dirs[d][0]
    y += dirs[d][1]
    return x, y, d
while len(st):
    x, y, d = st.pop()
    if x < 0 or x >= len(m[0]) or y < 0 or y >= len(m):
        continue
    seenspot.add((x, y))
    if m[y][x] == '/':
        ns = advance(x, y, d^1)
    elif m[y][x] == '\\':
        ns = advance(x, y, d^3)
    elif m[y][x] == '|' and d&1 == 0 or m[y][x] == '-' and d&1 == 1:
        ns = advance(x, y, (d-1)&3)
        if ns not in seen:
            seen.add(ns)
            st.append(ns)
        ns = advance(x, y, (d+1)&3)
    else:
        ns = advance(x, y, d)
    if ns not in seen:
        seen.add(ns)
        st.append(ns)
print(len(seenspot))
