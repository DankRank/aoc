#!/usr/bin/env python3
seeds = [int(x) for x in input().split(': ')[1].split()]
input()
input()
m = {}
def dostage():
    for i, seed in enumerate(seeds):
        for k, v in m.items():
            if seed in k:
                seeds[i] += v
                break
try:
    while True:
        line = input()
        if line == '':
            dostage()
            m = {}
            input()
            continue
        dst, src, size = (int(x) for x in line.split())
        m[range(src,src+size)] = dst-src
except EOFError:
    pass
dostage()
print(min(seeds))
