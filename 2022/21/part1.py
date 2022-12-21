#!/usr/bin/env python3
mapp = {}
try:
    while True:
        line = input().split()
        if len(line) < 3:
            mapp[line[0][:-1]] = {'res': int(line[1])}
        elif line[2] == '+':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a+b}
        elif line[2] == '-':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a-b}
        elif line[2] == '*':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a*b}
        elif line[2] == '/':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a//b}
except EOFError:
    pass

for m in mapp.values():
    if m['res'] is None:
        m['a'] = mapp[m['a']]
        m['b'] = mapp[m['b']]

while mapp['root']['res'] is None:
    progress = 0
    for m in mapp.values():
        if m['res'] is None and m['a']['res'] is not None and m['b']['res'] is not None:
            m['res'] = m['op'](m['a']['res'], m['b']['res'])
            progress += 1
    assert progress > 0
print(mapp['root']['res'])
