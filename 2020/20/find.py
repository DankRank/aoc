#!/usr/bin/env python3
import sys

snake = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]]

pic = []
back = []
inf = sys.stdin
for i in range(96):
    pic.append([])
    back.append([])
    line = inf.readline().rstrip()
    for j in range(96):
        pic[i].append(1 if line[j] == '#' else 0)
        back[i].append(1 if line[j] == '#' else 0)

def flipx(arr):
    arr2 = [i.copy() for i in arr]
    for i in arr2:
        i.reverse()
    return arr2
def flipy(arr):
    arr2 = [i.copy() for i in arr]
    arr2.reverse()
    return arr2
def flipd(arr):
    return [list(x) for x in zip(*arr)]

count_snek = 0
def checkone(x,y):
    for i in range(sh):
        for j in range(sw):
            if snake[i][j] and not pic[y+i][x+j]:
                return False
    return True
def check():
    global sh, sw
    sh = len(snake)
    sw = len(snake[0])
    for y in range(96):
        if y+sh >= 96:
            break
        for x in range(96):
            if x+sw >= 96:
                break
            if checkone(x, y):
                global count_snek
                count_snek += 1
                for i in range(sh):
                    for j in range(sw):
                        if snake[i][j]:
                            back[y+i][x+j] = 0

check() # identity
snake = flipx(snake)
check() # flipx
snake = flipy(snake)
check() # flipx flipy
snake = flipx(snake)
check() # flipy
snake = flipd(flipy(snake))
check() # flipd
snake = flipx(snake)
check() # flipd flipx
snake = flipy(snake)
check() # flipd flipx flipy
snake = flipx(snake)
check() # flipd flipy

total = 0
for i in range(96):
    for j in range(96):
        if back[i][j]:
            total += 1
print(total)
