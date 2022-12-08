#!/usr/bin/env python3
W=99
mapp = []
try:
    while True:
        mapp.append(list(map(int, input())))
except EOFError:
    pass
visible = set()
def check_visibility(sx, sy, dx, dy):
    tallest = -1
    global visible
    for i in range(W):
        h = mapp[sy][sx]
        if h > tallest:
            tallest = h
            visible.add((sx,sy))
        sx += dx
        sy += dy
#def show_visibility():
#    s = ""
#    for y in range(W):
#        for x in range(W):
#            if (x, y) in visible:
#                s += f'\x1b[1;32m{mapp[y][x]}\x1b[m'
#            else:
#                s += str(mapp[y][x])
#        s += '\n'
#    print(s)
for i in range(W):
    check_visibility(0, i, 1, 0)
    check_visibility(W-1, i, -1, 0)
    check_visibility(i, 0, 0, 1)
    check_visibility(i, W-1, 0, -1)
print(len(visible))
