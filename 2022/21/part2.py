#!/usr/bin/env python3
mapp = {}
try:
    while True:
        line = input().split()
        if len(line) < 3:
            mapp[line[0][:-1]] = {'res': int(line[1])}
        elif line[2] == '+':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a+b, 'iopl': lambda c, a: c-a, 'iopr': lambda c, b: c-b}
        elif line[2] == '-':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a-b, 'iopl': lambda c, a: a-c, 'iopr': lambda c, b: c+b}
        elif line[2] == '*':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a*b, 'iopl': lambda c, a: c//a, 'iopr': lambda c, b: c//b}
        elif line[2] == '/':
            mapp[line[0][:-1]] = {'res': None, 'a': line[1], 'b': line[3], 'op': lambda a, b: a//b, 'iopl': lambda c, a: a//c, 'iopr': lambda c, b: c*b}
except EOFError:
    pass

for m in mapp.values():
    if m['res'] is None:
        m['a'] = mapp[m['a']]
        m['b'] = mapp[m['b']]

mapp['root']['op'] = None
mapp['humn']['res'] = None
mapp['humn']['a'] = mapp['humn']
mapp['humn']['b'] = mapp['humn']

while mapp['root']['a']['res'] is None and mapp['root']['b']['res'] is None:
    progress = 0
    for m in mapp.values():
        if m['res'] is None and m['a']['res'] is not None and m['b']['res'] is not None:
            m['res'] = m['op'](m['a']['res'], m['b']['res'])
            progress += 1
    assert progress > 0
if mapp['root']['a']['res'] is None:
    m = mapp['root']['a']
    num = mapp['root']['b']['res']
    assert num is not None
else:
    m = mapp['root']['b']
    num = mapp['root']['a']['res']
    assert num is not None

while m != mapp['humn']:
    assert m['a']['res'] is not None or m['b']['res'] is not None
    if m['a']['res'] is not None:
        num = m['iopl'](num, m['a']['res'])
        m = m['b']
    else:
        num = m['iopr'](num, m['b']['res'])
        m = m['a']
print(num)
