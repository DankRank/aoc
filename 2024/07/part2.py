#!/usr/bin/env python3
import sys
def parseline(line):
    a, b = line.rstrip().split(': ')
    return int(a), [int(x) for x in b.split()]
m = [parseline(line) for line in sys.stdin]

assert all(x < 1000 for a, b in m for x in b)

total = 0
class Found(Exception): pass
def concat(a, b):
    if b < 10:
        return a*10 + b
    elif b < 100:
        return a*100 + b
    elif b < 1000:
        return a*1000 + b
    raise ValueError('bad assumption')
for res, nums in m:
    def dfs(val, i):
        if val > res:
            return
        elif i == len(nums):
            if val == res:
                raise Found()
        else:
            dfs(val+nums[i], i+1)
            dfs(val*nums[i], i+1)
            dfs(concat(val, nums[i]), i+1)
    try:
        dfs(nums[0], 1)
    except Found:
        total += res
print(total)
