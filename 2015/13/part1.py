#!/usr/bin/env python3
import itertools
rates = {}
names = 'ABCDEFGM'
for i in names+'U':
    for j in names+'U':
        if i != j:
            rates[(i,j)] = 0
try:
    while True:
        line = input().split()
        i = line[0][0]
        j = line[10][0]
        n = int(line[3])
        if line[2] == "lose":
            n *= -1
        rates[(i,j)] += n
        rates[(j,i)] += n
except EOFError:
    pass
print(max(sum(rates[p[i],p[(i+1)%len(p)]] for i in range(len(p))) for p in itertools.permutations(names)))
print(max(sum(rates[p[i],p[(i+1)%len(p)]] for i in range(len(p))) for p in itertools.permutations(names+'U')))
