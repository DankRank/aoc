#!/usr/bin/env python3
x = 0
y = 0
aim = 0
try:
    while True:
        command, dist = input().split()
        dist = int(dist)
        if command == "forward":
            x += dist
            y += aim*dist
        elif command == "down":
            aim += dist
        elif command == "up":
            aim -= dist
except EOFError:
    pass
print(x*y)
