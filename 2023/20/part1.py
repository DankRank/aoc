#!/usr/bin/env python3
import functools
numerics = {'broadcaster':0}
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

#rn = {v: k for k, v in numerics.items()}
#rn[-1] = 'button'
def pushbutton(state):
    st = [(0, 0, -1)]
    hcount, lcount = 0, 0
    while len(st):
        i, x, src = st[0]
        #print(rn[src], '-high->' if x else '-low->', rn[i])
        if x:
            hcount += 1
        else:
            lcount += 1
        del st[0]
        if types[i] == '%':
            if x == 0:
                state[i] ^= 1
                st += [(j, state[i], i) for j in outputs[i]]
        elif types[i] == '&':
            state[i][inputsidx[i, src]] = x
            if all(state[i]):
                st += [(j, 0, i) for j in outputs[i]]
            else:
                st += [(j, 1, i) for j in outputs[i]]
        elif i == 0: # broadcast
            st += [(j, x, i) for j in outputs[i]]
    return state, hcount, lcount
            
hcount, lcount = 0, 0
for i in range(1000):
    state, h, l = pushbutton(state)
    hcount += h
    lcount += l
print(hcount*lcount)
