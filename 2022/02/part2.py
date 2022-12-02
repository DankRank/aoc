#!/usr/bin/env python3
score = 0
try:
    while True:
        a, b = map(ord, input().split())
        a -= ord("A")
        b -= ord("X")
        score += b*3
        score += (a+b+2)%3 + 1
except EOFError:
    pass
print(score)
