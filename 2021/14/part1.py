#!/usr/bin/env python3
from collections import Counter
rules = {}
template = input()
input()
try:
    while True:
        ab, c = input().split(' -> ')
        rules[ab[0], ab[1]] = c
except EOFError:
    pass

def step(s):
    ns = ""
    for i in range(len(s)-1):
        ns += s[i]
        if (s[i], s[i+1]) in rules:
            ns += rules[s[i], s[i+1]]
    ns += s[len(s)-1]
    return ns

for i in range(10):
    template = step(template)
elements = Counter(template).most_common()
_, most_common = elements[0]
_, least_common = elements[-1]
print(most_common - least_common)
