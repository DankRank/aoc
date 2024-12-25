#!/usr/bin/env python3
m = []
currentm = []
try:
    while True:
        line = input()
        if line == '':
            m.append(currentm)
            currentm = []
        else:
            currentm.append(line)
except EOFError:
    pass
m.append(currentm)

w = len(m[0][0])
h = len(m[0])-2

locks = []
keys = []

for keylock in m:
    transposed = zip(*keylock)
    cols = [col.count('#')-1 for col in zip(*keylock)]
    if keylock[0] == '#'*w:
        locks.append(cols)
    else:
        keys.append(cols)

def fit(lock, key):
    return all(lock[i]+key[i] <= h for i in range(w))

count = sum(1 for lock in locks for key in keys if fit(lock, key))
print(count)
