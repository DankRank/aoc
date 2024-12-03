#!/usr/bin/env python3
import re
import sys
res = 0
en = True
for m in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)', sys.stdin.read()):
    if m.group() == 'do()':
        en = True
    elif m.group() == 'don\'t()':
        en = False
    elif en:
        res += int(m.group(1))*int(m.group(2))
print(res)
