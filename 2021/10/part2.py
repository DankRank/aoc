#!/usr/bin/env python3
from functools import reduce
from statistics import median
ocmap = { '(': ')', '[': ']', '{': '}', '<': '>' }
scoremap = { ')': 1, ']': 2, '}': 3, '>': 4 }
scores = []
try:
    while True:
        stack = []
        s = input()
        corrupted = False
        for c in s:
            if c in ocmap:
                stack.append(ocmap[c])
            elif c != stack.pop():
                corrupted = True
                break
        if not corrupted:
            scores.append(reduce(lambda x, y: x*5 + y, (scoremap[x] for x in reversed(stack)), 0))
except EOFError:
    pass
print(median(scores))
