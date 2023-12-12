#!/usr/bin/env python3
import functools
def solve(l, r):
    trueish = [x != '.' for x in l]
    falseish = [x != '#' for x in l] + [True]
    potentials = set()
    for i in range(len(l)):
        if i != 0 and l[i-1] == '#':
            continue
        for j in range(i+1, len(l)+1):
            if l[j-1] == '.':
                break
            if j == len(l) or l[j] != '#':
                potentials.add((i, j))
    @functools.cache
    def rec(i, j):
        if i == len(r):
            if '#' in l[j:]:
                return 0
            return 1
        arity = r[i]
        count = 0
        while j < len(l):
            if (j, j+arity) in potentials:
                count += rec(i+1, j+arity+1)
            if l[j] == '#':
                break
            j += 1
        return count
    return rec(0, 0)
s = 0
try:
    while True:
        l, r = input().split(' ')
        s += solve('?'.join(5*[l]), 5*[int(x) for x in r.split(',')])
except EOFError:
    pass
print(s)
