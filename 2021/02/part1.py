#!/usr/bin/env python3
x = 0
y = 0
try:
    while True:
        command, dist = input().split()
        dist = int(dist)
        if command == "forward":
            x += dist
        elif command == "down":
            y += dist
        elif command == "up":
            y -= dist
except EOFError:
    pass
print(x*y)
