#!/usr/bin/env python3
total = 0
def priority(s):
    if s < 'a':
        return ord(s) - ord('A') + 27
    else:
        return ord(s) - ord('a') + 1
try:
    while True:
        a = set(input())
        b = set(input())
        c = set(input())
        total += priority(a.intersection(b).intersection(c).pop())
except EOFError:
    pass
print(total)
