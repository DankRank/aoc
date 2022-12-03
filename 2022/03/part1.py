#!/usr/bin/env python3
total = 0
def priority(s):
    if s < 'a':
        return ord(s) - ord('A') + 27
    else:
        return ord(s) - ord('a') + 1
try:
    while True:
        line = input()
        a = set(line[:len(line)//2])
        b = set(line[len(line)//2:])
        total += priority(a.intersection(b).pop())
except EOFError:
    pass
print(total)
