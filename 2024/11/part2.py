#!/usr/bin/env python3
import functools
m = [int(x) for x in input().split()]

@functools.cache
def step(x, times):
    if times == 0:
        return 1
    if x == 0:
        return step(1, times-1)
    else:
        digits = len(str(x))
        if digits % 2 == 0:
            a, b = divmod(x, 10**(digits//2))
            return step(a, times-1) + step(b, times-1)
        else:
            return step(2024*x, times-1)
    return n

print(sum(step(x, 75) for x in m))
