#!/usr/bin/env python3
code = []
pos = 5
try:
    while True:
        for i in input():
            if i == 'U':
                if pos == 13 or pos == 3:
                    pos -= 2
                elif pos >= 6 and pos <= 12 and pos != 9:
                    pos -= 4
            elif i == 'D':
                if pos == 1 or pos == 11:
                    pos += 2
                elif pos >= 2 and pos <= 8 and pos != 5:
                    pos += 4
            elif i == 'L':
                if pos not in {1, 2, 5, 10, 13}:
                    pos -= 1
            elif i == 'R':
                if pos not in {1, 4, 9, 12, 13}:
                    pos += 1
        code.append(f'{pos:X}')
except EOFError:
    pass
print(''.join(code))
