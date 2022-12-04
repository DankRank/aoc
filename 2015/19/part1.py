#!/usr/bin/env python3
rules = []
try:
    while True:
        line = input()
        if line == '':
            pattern = input()
            break
        else:
            k, _, v = line.split()
            rules.append((k, v))
except EOFError:
    pass
results = set()
for k, v in rules:
    i = 0
    while True:
        i = pattern.find(k, i)
        if i == -1:
            break
        results.add(pattern[:i]+v+pattern[i+len(k):])
        i += 1
print(len(results))
