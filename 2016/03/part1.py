#!/usr/bin/env python3
count = 0
try:
    while True:
        a, b, c = map(int, input().split())
        if a + b > c and a + c > b and b + c > a:
            count += 1
except EOFError:
    pass
print(count)
