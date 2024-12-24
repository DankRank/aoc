#!/usr/bin/env python3
known = {}
unknown = {}
try:
    while True:
        line = input()
        if line == '':
            break
        k, v = line.split(': ')
        known[k] = int(v)
    while True:
        line = input()
        a, op, b, _, c = line.split()
        unknown[c] = (op, a, b)
except EOFError:
    pass

while len(unknown):
    for k, v in unknown.copy().items():
        if v[1] in known and v[2] in known:
            if v[0] == 'AND':
                known[k] = int(known[v[1]] and known[v[2]])
            elif v[0] == 'OR':
                known[k] = int(known[v[1]] or known[v[2]])
            elif v[0] == 'XOR':
                known[k] = int(known[v[1]] != known[v[2]])
            else:
                raise ValueError(f'unknown op {v[0]}')
            del unknown[k]

count = 0
i = 0
while True:
    key = f'z{i:02}'
    if key not in known:
        break
    if known[key]:
        count |= 1<<i
    i += 1
print(count)
