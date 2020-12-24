#!/usr/bin/env python3
import sys

mod = len(sys.argv[1])
input = [int(i)-1 for i in sys.argv[1]]
input.extend(range(mod, 1000000))
mod = 1000000

def step(ls, idx):
    c = ls[idx]
    a = [ls[(idx+1)%mod], ls[(idx+2)%mod], ls[(idx+3)%mod]]
    if idx+3 < mod:
        del ls[idx+1:idx+3+1]
    else:
        del ls[idx+1:]
        del ls[:idx+4-mod]
        idx -= idx+4-mod
    d = (c-1)%mod
    if d in a:
        d = (d-1)%mod
        if d in a:
            d = (d-1)%mod
            if d in a:
                d = (d-1)%mod
    dx = ls.index(d)
    ls[dx+1:dx+1] = a
    return idx+3 if dx<idx else idx

idx = 0
for i in range(1000000):
    print(i)
    idx = step(input, idx)

output = ''
idx = input.index(0)+1
print((input[(idx+1)%mod]+1) * (input[(idx+1)%mod]+1))
