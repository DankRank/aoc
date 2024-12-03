#!/usr/bin/env python3
import re
import sys
res = 0
for m in re.finditer(r'mul\((\d+),(\d+)\)', sys.stdin.read()):
    res += int(m.group(1))*int(m.group(2))
print(res)
