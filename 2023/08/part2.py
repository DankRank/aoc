#!/usr/bin/env python3
path = input()
m = {}
input()
try:
    while True:
        k, v = input().rstrip(')').split(' = (')
        m[k] = v.split(', ')
except EOFError:
    pass
startpoints = [s for s in m if s.endswith('A')]
def analyze(s):
    seen = {}
    ends = []
    i = 0
    count = 0
    seen[s, i] = count
    while True:
        di = path[i]
        s = m[s][int(di == 'R')]
        i += 1
        count += 1
        if (s, i) in seen:
            break
        if s.endswith('Z'):
            ends.append(count)
        seen[s, i] = count
        i %= len(path)
    return seen[s, i], count, ends

offset = []
modulo = []
ends = []
for i in startpoints:
    a, b, c = analyze(i)
    assert len(c) == 1 # only one end on each loop
    offset.append(a)
    modulo.append(b - a)
    ends.append(c[0] - a)
maxoffset = max(offset)
for i in range(len(ends)):
    ends[i] -= (maxoffset-offset[i])
    ends[i] %= modulo[i]
# fun fact 1: all moduli are divisible by len(path)
# fun fact 2: after division, modulos will be prime
assert all(i%len(path) == 0 for i in modulo)
for i, v in enumerate(modulo):
    modulo[i] = v//len(path)
# fun fact 3: the ends are congruent modulo len(path)
endsoffset = ends[0]%len(path)
assert all(endsoffset == i%len(path) for i in ends)
for i, v in enumerate(ends):
    ends[i] = v//len(path)

def crt(a1, m1, a2, m2):
    n1 = pow(m1, -1, m2)
    n2 = pow(m2, -1, m1)
    m = m1*m2
    return (a1*n2*m2 + a2*n1*m1)%m, m
for i in range(1, len(modulo)):
    ends[0], modulo[0] = crt(ends[0], modulo[0], ends[i], modulo[i])

print(maxoffset + ends[0]*len(path) + endsoffset)
