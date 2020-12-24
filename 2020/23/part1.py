#!/usr/bin/env python3
import sys

mod = len(sys.argv[1])
input = [int(i)-1 for i in sys.argv[1]]

def step(ls, idx):
    c = ls[idx]
    a1 = ls.pop(idx+1 if idx+1<mod else 0)
    a2 = ls.pop(idx+1 if idx+2<mod else 0)
    a3 = ls.pop(idx+1 if idx+3<mod else 0)
    a = [a1, a2, a3]
    d = (c-1)%mod
    if d in a:
        d = (d-1)%mod
        if d in a:
            d = (d-1)%mod
            if d in a:
                d = (d-1)%mod
    dx = ls.index(d)
    ls[dx+1:dx+1] = a
    return (ls.index(c)+1)%mod

idx = 0
for i in range(100):
    idx = step(input, idx)

output = ''
idx = input.index(0)+1
for i in range(mod-1):
    output += str(input[(idx+i)%mod]+1)
print(output)
