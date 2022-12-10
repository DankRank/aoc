#!/usr/bin/env python3
x = 1
cycle = 0
scan = 0
s = [[]]
def draw():
    global cycle
    global scan
    if cycle == 40:
        cycle = 0
        scan += 1
        s.append([])
    s[scan].append('#' if x in (cycle-1, cycle, cycle+1) else ' ')
    cycle += 1
try:
    while True:
        line = input().split()
        if line[0] == 'addx':
            draw()
            draw()
            x += int(line[1])
        elif line[0] == 'noop':
            draw()
except EOFError:
    pass
print('\n'.join(''.join(line) for line in s))
