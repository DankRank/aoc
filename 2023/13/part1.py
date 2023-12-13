#!/usr/bin/env python3
m = []
def solvepass(m):
    for i in range(1, len(m)):
        j = 0
        while i+j in range(len(m)) and i-j-1 in range(len(m)):
            if m[i+j] != m[i-j-1]:
                break
            j += 1
        else:
            return i
    return None
def solve(m):
    sol = solvepass(m)
    if sol is not None:
        return sol*100
    mt = [''.join(x) for x in zip(*m)]
    return solvepass(mt)

s = 0
try:
    while True:
        line = input()
        if line == '':
            s += solve(m)
            m = []
        else:
            m.append(line)
except EOFError:
    pass
s += solve(m)
print(s)
