#!/usr/bin/env python3
s = input()
p = 0
count = 0
while p < len(s):
    lp = s.find('(', p)
    if lp == -1:
        count += len(s)-p
        break
    count += lp - p
    rp = s.find(')', lp)
    a, b = map(int, s[lp+1:rp].split('x'))
    count += a*b
    p = rp+1+a
print(count)
