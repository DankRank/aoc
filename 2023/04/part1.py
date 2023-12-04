#!/usr/bin/env python3
s = 0
try:
    while True:
        win, have = input().split(': ')[1].replace('  ', ' ').lstrip().split(' | ')
        win = set(int(x) for x in win.split())
        have = set(int(x) for x in have.split())
        s += int(2**(len(win & have)-1))
except EOFError:
    pass
print(s)
