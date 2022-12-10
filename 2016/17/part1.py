#!/usr/bin/env python3
import functools
import hashlib
import sys
passcode = input().encode()
@functools.lru_cache(10)
def pathxy(p):
    return p.count('R')-p.count('L'), p.count('D')-p.count('U')
def isvalid(p):
    x, y = pathxy(p)
    return x >= 0 and x < 4 and y >= 0 and y < 4
def derive(p):
    h = hashlib.md5()
    h.update(passcode)
    h.update(p.encode())
    return (p+y for x, y in zip(h.hexdigest()[:4], 'UDLR') if x in 'bcdef' if isvalid(p+y))

last_paths = set()
next_paths = {''}
while True:
    last_paths, next_paths = next_paths, set()
    for p in last_paths:
        for p in derive(p):
            if pathxy(p) == (3, 3):
                print(p)
                sys.exit(0)
            next_paths.add(p)
