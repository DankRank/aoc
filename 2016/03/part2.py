#!/usr/bin/env python3
count = 0
try:
    while True:
        x = map(int, input().split())
        y = map(int, input().split())
        z = map(int, input().split())
        for a, b, c in zip(x, y, z):
            if a + b > c and a + c > b and b + c > a:
                count += 1
except EOFError:
    pass
print(count)
