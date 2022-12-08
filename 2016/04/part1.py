#!/usr/bin/env python3
from collections import Counter
count = 0
try:
    while True:
        line = input().rstrip(']').split('-')
        name = ''.join(line[:-1])
        idn, cksum = line[-1].split('[')
        cksum2 = ''.join(map(lambda x: x[0], sorted(Counter(name).items(), key=lambda x: (-x[1], x[0]))[:5]))
        if cksum == cksum2:
            count += int(idn)
except EOFError:
    pass
print(count)
