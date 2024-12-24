#!/usr/bin/env python3
m = []
try:
    while input() != '':
        pass
    while True:
        line = input()
        a, op, b, _, c = line.split()
        m.append([op, a, b, c])
except EOFError:
    pass

def swapoutput(x, y):
    for i in range(len(m)):
        if m[i][3] == x:
            m[i][3] = y
        elif m[i][3] == y:
            m[i][3] = x

swapoutput('hcc', 'z11') # carry12 z11
swapoutput('hqc', 'qcw') # and24 xor24
swapoutput('fdw', 'z35') # and35 z35
swapoutput('bpf', 'z05') # halfcarry05 z05

safenames = set()
for i in range(46):
    safenames.add(f'x{i:02}')
    safenames.add(f'y{i:02}')
    safenames.add(f'z{i:02}')

prerename = {}
def rename(old, new):
    if old in prerename:
        prerename[new] = prerename[old]
    else:
        prerename[new] = old
    for i in range(len(m)):
        for j in range(1, 4):
            if m[i][j] == old:
                m[i][j] = new

todel = []
for i, (op, a, b, c) in enumerate(m):
    if a > b:
        a, b = b, a
    if c not in safenames:
        if a[0] == 'x' and b[0] == 'y' and a[1:].isdigit() and a[1:] == b[1:]:
            rename(c, op.lower() + a[1:])
            todel.append(i)

for i in reversed(todel):
    del m[i]

def sortkey(s):
    if s in safenames:
        return (0, s)
    elif s.startswith('and') or s.startswith('or') or s.startswith('xor'):
        return (1, s)
    else:
        return (2, s)

for i, (op, a, b, c) in enumerate(m):
    if sortkey(a) > sortkey(b):
        a, b = b, a
    if c not in safenames:
        if op == 'OR' and a[:3] == 'and':
            rename(c, 'carry' + a[3:])

for (op, a, b, c) in m:
    if sortkey(a) > sortkey(b):
        a, b = b, a
    #print(f'{a} {op} {b} -> {c}')
print('bpf,fdw,hcc,hqc,qcw,z05,z11,z35')
