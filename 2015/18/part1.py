#!/usr/bin/env python3
# list is padded with borders like so:
# * * *
# * x x
# * x x
# * * * *
ls1 = [0]*101
ls2 = [0]*(101*102+1)
try:
    while True:
        ls1 += map(lambda x: 1 if x == '#' else 0, '.'+input())
except EOFError:
    pass
ls1 += [0]*102
def neighbors(i):
    return ls1[i-102] + ls1[i-101] + ls1[i-100] + ls1[i-1] + ls1[i+1] + ls1[i+100] + ls1[i+101] + ls1[i+102]
for t in range(100):
    for i in range(102, 101*101, 101):
        for j in range(i, i+100):
            n = neighbors(j)
            if n == 3:
                ls2[j] = 1
            elif n != 2:
                ls2[j] = 0
            else:
                ls2[j] = ls1[j]
    ls1, ls2 = ls2, ls1
print(sum(ls1))
