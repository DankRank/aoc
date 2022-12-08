#!/usr/bin/env python3
from collections import Counter
ctrs = [Counter() for i in range(8)]
try:
    while True:
        for ctr, c in zip(ctrs, input()):
            ctr[c] -= 1
except EOFError:
    pass
print(''.join(map(lambda x: x.most_common()[0][0], ctrs)))
