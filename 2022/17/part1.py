#!/usr/bin/env python3
line = input()
jeti = 0
mapp = []
def next_move():
    global jeti
    move = -1 if line[jeti] == '<' else 1
    jeti += 1
    jeti %= len(line)
    return move
def check_free(x, y):
    if x < 0 or x >= 7:
        return False
    if y < 0:
        return False
    if y >= len(mapp):
        return True
    return not mapp[y][x]
def can_move(pid, x, y):
    if pid == 0:
        return check_free(x, y) and check_free(x+1, y) and check_free(x+2, y) and check_free(x+3, y)
    if pid == 1:
        return check_free(x+1, y) and check_free(x, y+1) and check_free(x+1, y+1) and check_free(x+2, y+1) and check_free(x+1, y+2)
    if pid == 2:
        return check_free(x, y) and check_free(x+1, y) and check_free(x+2, y) and check_free(x+2, y+1) and check_free(x+2, y+2)
    if pid == 3:
        return check_free(x, y) and check_free(x, y+1) and check_free(x, y+2) and check_free(x, y+3)
    if pid == 4:
        return check_free(x, y) and check_free(x, y+1) and check_free(x+1, y) and check_free(x+1, y+1)
def ensure_height(h):
    while len(mapp) < h:
        mapp.append([0]*7)
def place(pid, x, y):
    if pid == 0:
        ensure_height(y+1)
        mapp[y][x] = 1
        mapp[y][x+1] = 1
        mapp[y][x+2] = 1
        mapp[y][x+3] = 1
    elif pid == 1:
        ensure_height(y+3)
        mapp[y][x+1] = 1
        mapp[y+1][x] = 1
        mapp[y+1][x+1] = 1
        mapp[y+1][x+2] = 1
        mapp[y+2][x+1] = 1
    elif pid == 2:
        ensure_height(y+3)
        mapp[y][x] = 1
        mapp[y][x+1] = 1
        mapp[y][x+2] = 1
        mapp[y+1][x+2] = 1
        mapp[y+2][x+2] = 1
    elif pid == 3:
        ensure_height(y+4)
        mapp[y][x] = 1
        mapp[y+1][x] = 1
        mapp[y+2][x] = 1
        mapp[y+3][x] = 1
    elif pid == 4:
        ensure_height(y+2)
        mapp[y][x] = 1
        mapp[y][x+1] = 1
        mapp[y+1][x] = 1
        mapp[y+1][x+1] = 1
def print_board():
    for i in mapp[-1::-1]:
        print('|'+''.join('#' if j else '.' for j in i)+'|')
    print('+'+'-'*7+'+')
for i in range(2022):
    x, y = 2, len(mapp)+3
    while True:
        m = next_move()
        if can_move(i%5, x+m, y):
            x += m
        if can_move(i%5, x, y-1):
            y -= 1
        else:
            place(i%5, x, y)
            break
print(len(mapp))
