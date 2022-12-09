#!/usr/bin/env python3
import re
from itertools import chain
def aba(s):
    return map(lambda x: x[1]+x[0]+x[1], filter(lambda x: x[0] != x[1] and x[0] == x[2], zip(s, s[1:], s[2:])))
count = 0
try:
    while True:
        line = re.split('[][]',input())
        abas = chain.from_iterable(aba(s) for s in line[::2])
        if any(any(aba in s for s in line[1::2]) for aba in abas):
            count += 1
except EOFError:
    pass
print(count)
