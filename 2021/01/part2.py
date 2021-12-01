#!/usr/bin/env python3
count = 0
a = int(input())
b = int(input())
c = int(input())
try:
    while True:
        d = int(input())
        if b+c+d > a+b+c:
            count += 1
        a,b,c = b,c,d
except EOFError:
    pass
print(count)
