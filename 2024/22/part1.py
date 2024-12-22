#!/usr/bin/env python3
import sys
m = [int(line.rstrip()) for line in sys.stdin]

def nextnum(i):
    i = (i^(i<<6)) & 0xffffff
    i = (i^(i>>5)) & 0xffffff
    i = (i^(i<<11)) & 0xffffff
    return i

count = 0
for s in m:
    for i in range(2000):
        s = nextnum(s)
    count += s
print(count)
