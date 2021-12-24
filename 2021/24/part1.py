#!/usr/bin/env python3
from itertools import product
def expand(i):
    return (
        i[0],
        i[1],
        i[2],
        i[2] + 16 - 8,
        i[1] + 1 - 4,
        i[3],
        i[4],
        i[5],
        i[5] + 15 - 13,
        i[4] + 2 - 3,
        i[3] + 3 - 7,
        i[6],
        i[6] + 1 - 6,
        i[0] + 1 - 8,
    )
results = []
for i in product(range(1,10), repeat=7):
    expanded = expand(i)
    if all(d > 0 and d < 10 for d in expanded):
        results.append(expanded)
results.sort()
print(''.join(str(x) for x in max(results)))
print(''.join(str(x) for x in min(results)))
