#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def solve(x, y, d):
    st = [(x, y, d)]
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
    return len(seenspot)

a = max(solve(0, i, 0) for i in range(len(m)))
b = max(solve(len(m[0])-1, i, 2) for i in range(len(m)))
c = max(solve(i, 0, 3) for i in range(len(m[0])))
d = max(solve(i, len(m)-1, 1) for i in range(len(m[0])))
print(max(a, b, c, d))
