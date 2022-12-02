#!/usr/bin/env python3
score = 0
try:
    while True:
        a, b = map(ord, input().split())
        a -= ord("A")
        b -= ord("X")
        score += b+1
        if a == b:
            score += 3
        elif (a+1)%3 == b:
            score += 6
except EOFError:
    pass
print(score)
