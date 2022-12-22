#!/usr/bin/env python3
import re
mapp = []
while True:
    line = input()
    if line == '':
        break
    mapp.append(line)

maxw = max(len(x) for x in mapp)
for i,v in enumerate(mapp):
    if maxw > len(v):
        mapp[i] += (maxw - len(v))*' '

ffront = (50, 0)
fright = (100, 0)
fbottom = (50, 50)
fback = (50, 100)
fleft = (0, 100)
ftop = (0, 150)
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
# clockwise order
def gen_side(f, s, ofs=0):
    x, y = f
    if s == RIGHT:
        for i in range(50):
            yield x+49+ofs, y+i
    elif s == DOWN:
        for i in range(50):
            yield x+49-i, y+49+ofs
    elif s == LEFT:
        for i in range(50):
            yield x-ofs, y+49-i
    elif s == UP:
        for i in range(50):
            yield x+i, y-ofs

stitches = {}
def stitch(f1, s1, f2, s2):
    for p1, p2 in zip(gen_side(f1, s1, 1), reversed(list(gen_side(f2, s2)))):
        assert p1 != p2 or s1 == s2^2
        if p1 != p2:
            assert p1 + (s1,) not in stitches
            stitches[p1 + (s1,)] = p2 + (s2^2,)
def stitch2(f1, s1, f2, s2):
    stitch(f1, s1, f2, s2)
    stitch(f2, s2, f1, s1)
# TODO: All of this can probably be derived from orientation of the faces
stitch2(ffront, RIGHT, fright, LEFT)
stitch2(ffront, DOWN, fbottom, UP)
stitch2(ffront, LEFT, fleft, LEFT) # inverted
stitch2(ffront, UP, ftop, LEFT) # x=y
stitch2(fback, UP, fbottom, DOWN)
stitch2(fback, LEFT, fleft, RIGHT)
stitch2(fback, DOWN, ftop, RIGHT) #x=y
stitch2(fback, RIGHT, fright, RIGHT) # inverted
stitch2(ftop, DOWN, fright, UP)
stitch2(fright, DOWN, fbottom, RIGHT) # x=y
stitch2(fbottom, LEFT, fleft, UP) # x=y
stitch2(fleft, DOWN, ftop, UP)

cmds = re.sub('[LR]', r' \g<0> ', input()).split()
dx, dy = 1, 0
di = 0
x = re.search('[.#]', mapp[0]).span()[0]
y = 0
for cmd in cmds:
    if cmd == 'R':
        dx, dy, di = -dy, dx, (di+1)%4
    elif cmd == 'L':
        dx, dy, di = dy, -dx, (di-1)%4
    else:
        for i in range(int(cmd)):
            nx, ny, ndi = x+dx, y+dy, di
            if (nx, ny, di) in stitches:
                nx, ny, ndi = stitches[(nx, ny, di)]
            if mapp[ny][nx] == '.':
                if ndi != di:
                    dx, dy = 1, 0
                    for j in range(ndi):
                        dx, dy = -dy, dx
                x, y, di = nx, ny, ndi
print((y+1)*1000 + (x+1)*4 + di%4)
