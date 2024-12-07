#!/usr/bin/env python3
import sys
def parseline(line):
    a, b = line.rstrip().split(': ')
    return int(a), [int(x) for x in b.split()]
m = [parseline(line) for line in sys.stdin]

total = 0
class Found(Exception): pass
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
    try:
        dfs(nums[0], 1)
    except Found:
        total += res
print(total)
