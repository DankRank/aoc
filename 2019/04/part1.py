#!/usr/bin/env python3
a, b = (int(x) for x in input().split('-'))
a = [a//10**i%10 for i in range(5,-1,-1)]
b = [b//10**i%10 for i in range(5,-1,-1)]
for i in range(5):
    if a[i] > a[i+1]:
        a[i+1] = a[i]
count = 0
while a <= b:
    if any(x == y for x, y in zip(a, a[1:])):
        count += 1
    a[5] += 1
    i = 5
    while a[i] == 10 and i > 0:
        i -= 1
        a[i] += 1
    for i in range(i, 5):
        a[i+1] = a[i]
print(count)
