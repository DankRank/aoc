#!/usr/bin/env python3
def hash(s):
    h = 0
    for ch in s:
        h = ((h+ord(ch))*17)&255
    return h
print(sum(hash(s) for s in input().split(',')))
