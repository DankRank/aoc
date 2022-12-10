#!/usr/bin/env python3
x = 1
cycles = []
try:
    while True:
        line = input().split()
        if line[0] == 'addx':
            cycles.append(x)
            cycles.append(x)
            x += int(line[1])
        elif line[0] == 'noop':
            cycles.append(x)
except EOFError:
    pass
print(sum(a*b for a,b in zip(cycles[19::40], range(20, len(cycles)+1, 40))))
