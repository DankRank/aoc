#!/usr/bin/env python3
m = []
def solvepass(m):
    for i in range(1, len(m)):
        c = 0
        j = 0
        while i+j in range(len(m)) and i-j-1 in range(len(m)):
            if m[i+j] != m[i-j-1]:
                if c == 1:
                    break
                if sum(int(x!=y) for x, y in zip(m[i+j], m[i-j-1])) != 1:
                    break
                c += 1
            j += 1
        else:
            if c == 1: # ignore c == 0 because that's just the original solution
                return i
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
