#!/usr/bin/env python3
import re
s1, s2 = 0, 0
def mapdigit(x):
    m = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
    }
    return m[x] if x in m else x
try:
    while True:
        line = input()
        m = re.findall(r'\d', line)
        s1 += int(m[0]+m[-1])
        m = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        s2 += int(mapdigit(m[0])+mapdigit(m[-1]))
except EOFError:
    pass
print(s1)
print(s2)
