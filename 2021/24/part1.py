#!/usr/bin/env python3
from extract import *
import sys
from itertools import product
expand = eval(generate_expander(*extract_constants(sys.stdin)))
results = []
for i in product(range(1,10), repeat=7):
    expanded = expand(i)
    if all(d > 0 and d < 10 for d in expanded):
        results.append(expanded)
results.sort()
print(''.join(str(x) for x in max(results)))
print(''.join(str(x) for x in min(results)))
