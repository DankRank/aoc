#!/usr/bin/env python3
count = 0
first = int(input())
try:
    while True:
        second = int(input())
        if second > first:
            count += 1
        first = second
except EOFError:
    pass
print(count)
