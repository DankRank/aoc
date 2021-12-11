#!/usr/bin/env python3
count = 0
try:
    while True:
        inputs, outputs = map(lambda x: list(map(frozenset, x.split(' '))), input().split(' | '))
        known = [False]*10
        known[1] = next(x for x in inputs if len(x) == 2)
        known[7] = next(x for x in inputs if len(x) == 3)
        known[4] = next(x for x in inputs if len(x) == 4)
        known[8] = next(x for x in inputs if len(x) == 7)
        known[3] = next(x for x in inputs if len(x) == 5 and x > known[1])
        known[9] = next(x for x in inputs if len(x) == 6 and x > known[3])
        known[2] = next(x for x in inputs if len(x) == 5 and not x < known[9])
        known[6] = next(x for x in inputs if len(x) == 6 and not x > known[1])
        known[5] = next(x for x in inputs if len(x) == 5 and x < known[6])
        known[0] = next(x for x in inputs if len(x) == 6 and not x > known[5])
        solved = {known[i]: i for i in range(10)}
        count += int("".join(map(lambda x: str(solved[x]), outputs)))
except EOFError:
    pass
print(count)
