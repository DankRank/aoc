#!/usr/bin/env python3
import ast
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
count = 0
index = 1
try:
    while True:
        a = ast.literal_eval(input())
        b = ast.literal_eval(input())
        if not compare(b, a):
            count += index
        index += 1
        input()
except EOFError:
    pass
print(count)
