#!/usr/bin/env python3
cells = []
try:
    while True:
        cells.append(list(map(int, input())))
except EOFError:
    pass
def neighbors(i,j):
    if i != 0:
        if j != 0:
            yield i-1, j-1
        yield i-1, j
        if j != 9:
            yield i-1, j+1
    if j != 0:
        yield i, j-1
    if j != 9:
        yield i, j+1
    if i != 9:
        if j != 0:
            yield i+1, j-1
        yield i+1, j
        if j != 9:
            yield i+1, j+1
def step():
    flashed = set()
    def flash(i, j):
        flashed.add((i, j))
        for i, j in neighbors(i, j):
            if (i, j) not in flashed:
                cells[i][j] += 1
                if cells[i][j] == 10:
                    flash(i, j)
    for i in range(10):
        for j in range(10):
            cells[i][j] += 1
            if cells[i][j] == 10:
                flash(i, j)
    for i in range(10):
        for j in range(10):
            if cells[i][j] > 9:
                cells[i][j] = 0
    return len(flashed)
count = 0
for i in range(100):
    count += step()
print(count)
