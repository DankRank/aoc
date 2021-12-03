#!/usr/bin/env python3
ls = []
try:
    while True:
        ls.append(input())
except EOFError:
    pass
def countList(ls):
    counts = [0 for i in range(12)]
    for s in ls:
        for i in range(len(s)):
            counts[i] += 1 if s[i] == '1' else -1
    return counts
def filterList(ls, fn):
    for i in range(12):
        if len(ls) == 1:
            break
        counts = countList(ls)
        ls = list(filter(lambda x: fn(x[i] == '1', counts[i] >= 0), ls))
    return int(ls[0], 2)
oxy = filterList(ls, lambda x, y: x == y)
co2 = filterList(ls, lambda x, y: x != y)
print(oxy * co2)
