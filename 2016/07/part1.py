#!/usr/bin/env python3
import re
def abba(s):
    return any(a==d and b==c and a!=b for a, b, c, d in zip(s, s[1:], s[2:], s[3:]))
count = 0
try:
    while True:
        line = re.split('[][]',input())
        if any(abba(s) for s in line[::2]) and not any(abba(s) for s in line[1::2]):
            count += 1
except EOFError:
    pass
print(count)
