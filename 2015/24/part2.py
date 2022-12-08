#!/usr/bin/env python3
import sys
import itertools
import functools
import operator
weights = set(map(int, sys.stdin.read().splitlines()))
target = sum(weights)/4
for minlen in range(len(weights)+1):
    assert minlen < (len(weights)+3)//4
    ls = list(map(set, filter(lambda x: sum(x) == target, itertools.combinations(weights, minlen))))
    if len(ls) > 0:
        break
def can_balance(s):
    w = weights - s
    for l in range(minlen, (len(w)-minlen+2)//3):
        ls2 = list(map(set, filter(lambda x: sum(x) == target, itertools.combinations(w, l))))
        if len(ls2) > 0:
            for s2 in ls2:
                w2 = w - set(s2)
                for l2 in range(l, (len(w)-minlen-l+1)//2):
                    if next(filter(lambda x: sum(x) == target, itertools.combinations(w, l2)), False):
                        return True
    return False
print(min(map(lambda s: functools.reduce(operator.mul, s), filter(can_balance, ls))))
