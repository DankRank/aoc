#!/usr/bin/env python3
import functools
def compare(a,b):
    if isinstance(a, list) or isinstance(b, list):
        if not isinstance(a, list):
            a = [a]
        if not isinstance(b, list):
            b = [b]
        for i in range(min(len(a), len(b))):
            if compare(a[i], b[i]):
                return True
            if compare(b[i], a[i]):
                return False
        return len(a) < len(b)
    else:
        return a < b
def compare2(a,b):
    if compare(a, b):
        return -1
    if compare(b, a):
        return 1
    return 0
ls = []
ls.append([[2]])
ls.append([[6]])
try:
    while True:
        ls.append(eval(input()))
        ls.append(eval(input()))
        input()
except EOFError:
    pass
ls.sort(key=functools.cmp_to_key(compare2))
print((ls.index([[2]])+1)*(ls.index([[6]])+1))
