#!/usr/bin/env python3
lsls = []
ls = []
try:
    while True:
        line = input()
        if line == "":
            lsls.append(ls)
            ls = []
        else:
            ls.append(int(line))
except EOFError:
    pass
lsls.append(ls)
print(max(map(sum, lsls)))
