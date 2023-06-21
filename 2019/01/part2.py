#!/usr/bin/env python3
import sys
def fuel(f):
    s = 0
    while f > 0:
        s += f
        f = f//3 - 2
    return s
print(sum(fuel(int(line.rstrip())//3-2) for line in sys.stdin))
