#!/usr/bin/env python3
code = []
pos = 5
try:
    while True:
        for i in input():
            if i == 'U':
                if pos > 3:
                    pos -= 3
            elif i == 'D':
                if pos < 7:
                    pos += 3
            elif i == 'L':
                if pos%3 != 1:
                    pos -= 1
            elif i == 'R':
                if pos%3 != 0:
                    pos += 1
        code.append(str(pos))
except EOFError:
    pass
print(''.join(code))
