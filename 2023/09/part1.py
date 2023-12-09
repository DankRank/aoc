#!/usr/bin/env python3
s1, s2 = 0, 0
try:
    while True:
        vals = [int(x) for x in input().split()]
        derivs = [vals]
        while any(vals):
            vals = [b-a for a, b in zip(vals[:-1], vals[1:])]
            derivs.append(vals)
        vals.append(0)
        vals.insert(0, 0)
        for i in range(len(derivs)-1, 0, -1):
            derivs[i-1].append(derivs[i-1][-1] + derivs[i][-1])
            derivs[i-1].insert(0, derivs[i-1][0] - derivs[i][0])
        s1 += derivs[0][-1]
        s2 += derivs[0][0]
except EOFError:
    pass
print(s1)
print(s2)
