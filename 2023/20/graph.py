#!/usr/bin/env python3
import functools
numerics = {'broadcaster':0, 'rx':1}
def mapnumeric(s):
    if s in numerics:
        return numerics[s]
    else:
        numerics[s] = len(numerics)
        return numerics[s]
types = {}
outputs = {}
inputs = {}
inputsidx = {}
try:
    while True:
        l, r = input().split(' -> ')
        typ = l[0]
        if l[0] != 'b':
            l = l[1:]
        l = mapnumeric(l)
        r = [mapnumeric(s) for s in r.split(', ')]
        types[l] = typ
        outputs[l] = r
        for i in r:
            if i not in inputs:
                inputs[i] = [l]
            else:
                inputs[i].append(l)
except EOFError:
    pass
types[1] = 'b'
rn = {v: k for k, v in numerics.items()}

print('digraph {')
for i in numerics.values():
    if types[i] == '&':
        print(f'{rn[i]} [shape=rect]')
    if i in outputs:
        for j in outputs[i]:
            print(f'{rn[i]} -> {rn[j]}')
print('}')
