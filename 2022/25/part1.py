#!/usr/bin/env python3
def snafu_decode(s):
    num = 0
    m = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
    for i, j in enumerate(reversed(s)):
        num += 5**i * m[j]
    return num
def snafu_encode(num):
    s = []
    c = 0
    m = '012=-0'
    while num != 0:
        x = num%5 + c
        c = int(x > 2)
        s.append(m[x])
        num //= 5
    if c != 0:
        s.append('1')
    return ''.join(reversed(s))
total = 0
try:
    while True:
        total += snafu_decode(input())
except EOFError:
    pass
print(snafu_encode(total))
