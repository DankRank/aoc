#!/usr/bin/env python3
ls = []
try:
    while True:
        ls.append(tuple(int(s) for s in input().split('-')))
except EOFError:
    pass
ls.sort()
ols = None
while ols != ls:
    ols, ls = ls, []
    r = ols[0]
    for s in ols:
        if s[0] <= r[1]+1:
            r = (r[0], max(r[1], s[1]))
        else:
            ls.append(r)
            r = s
    ls.append(r)
print(ls[0][1]+1)
print(4294967296-sum(b-a+1 for a, b in ls))
