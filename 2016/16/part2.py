#!/usr/bin/env python3
import functools
@functools.lru_cache(1000)
def dragon(n): # A014707
    return dragon(n>>1) if n&1 else n>>1 & 1
line = input()
tlen = 35651584
assert len(line) == 17
assert tlen % 17 == 0
line = line+'0'+''.join('0' if x == '1' else '1' for x in reversed(line))+'0'
assert len(line) == 36
lineparity = line.count('1')%2
def slowparity(f, t):
    parity = 0
    for i in range(f, t):
        if i%36 == 17 or i%36 == 35:
            parity += dragon(i//18)
        else:
            parity += int(line[i%36])
    return parity
def fastparity(f, t):
    assert f%36 == 0 and t%36 == 0
    parity = 0
    for i in range(f, t, 36):
        parity += lineparity + dragon(i//18) + dragon(i//18 + 1)
    return parity
def calcparity(f, t):
    a = (f+35)//36*36
    b = t//36*36
    return slowparity(f, a)+fastparity(a, b)+slowparity(b, t)
res = ''
for i in range(0, tlen, tlen//17):
    res += str((calcparity(i, i+tlen//17)+1)%2)
print(res)
