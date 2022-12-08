#!/usr/bin/env python3
W=99
mapp = []
try:
    while True:
        mapp.append(list(map(int, input())))
except EOFError:
    pass
visible = set()
def check_side(h, sx, sy, dx, dy):
    count = 0
    while True:
        sx += dx
        sy += dy
        if sx < 0 or sx >= W or sy < 0 or sy >= W:
            break;
        count += 1
        if mapp[sy][sx] >= h:
            break
    return count
def score(sx, sy):
    return (check_side(mapp[sy][sx], sx, sy, 1, 0) *
            check_side(mapp[sy][sx], sx, sy, -1, 0) *
            check_side(mapp[sy][sx], sx, sy, 0, 1) *
            check_side(mapp[sy][sx], sx, sy, 0, -1))
print(max(score(x, y) for y in range(1, W-1) for x in range(1, W-1)))
