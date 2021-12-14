#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
rules = {}
template = input()
input()
try:
    while True:
        ab, c = input().split(' -> ')
        rules[ab[0], ab[1]] = c
except EOFError:
    pass

@lru_cache(maxsize=None)
def rec(a, b, level):
    counter = Counter()
    if (a,b) in rules:
        c = rules[a,b]
        counter[c] += 1
        if level > 1:
            counter += rec(a, c, level-1)
            counter += rec(c, b, level-1)
    return counter

counter = Counter(template)
for i in range(len(template)-1):
    counter += rec(template[i], template[i+1], 40)
elements = counter.most_common()
_, most_common = elements[0]
_, least_common = elements[-1]
print(most_common - least_common)
