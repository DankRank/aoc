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

state = []
for i in range(len(numerics)):
    if i not in types:
        types[i] = '0'
    if types[i] == '%':
        state.append(0)
    elif types[i] == '&':
        state.append([0]*len(inputs[i]))
        for idx, j in enumerate(inputs[i]):
            inputsidx[i, j] = idx
    else:
        state.append(None)

count = 1
for i in outputs[0]:
    node = [j for j in outputs[i] if types[j] == '&'][0]
    trigger = ''
    addend = ''
    while i is not None:
        assert types[i] == '%'
        assert len(outputs[i]) <= 2
        assert len(inputs[i]) <= 2
        assert len(outputs[i]) < 2 or node in outputs[i]
        assert len(inputs[i]) < 2 or node in inputs[i]
        trigger += '1' if node in outputs[i] else '0'
        addend += '1' if node in inputs[i] else '0'
        i = [j for j in outputs[i] if j != node]
        i = i[0] if len(i) else None
    bits = len(trigger)
    trigger = int(trigger[::-1], 2)
    addend = int(addend[::-1], 2)
    assert bin(trigger+addend) == '0b1'+'0'*bits
    assert all(trigger%i for i in range(2, trigger)) # is prime?
    count *= trigger
print(count)
