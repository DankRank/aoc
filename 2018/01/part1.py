#!/usr/bin/env python3
import sys
m = [int(line.rstrip()) for line in sys.stdin]

print(sum(m))

def find():
    known = {0}
    f = 0
    while True:
        for d in m:
            f += d
            if f in known:
                return f
            known.add(f)

print(find())
