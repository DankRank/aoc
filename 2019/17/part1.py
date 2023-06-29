#!/usr/bin/env python3
from intcode import *
vm = IntcodeVM(parsetext(input()))
vm.run()
m = ''.join(chr(x) for x in vm.outq).split()
s = 0
for y in range(1, len(m)-1):
    for x in range(1, len(m[y])-1):
        if m[y-1][x] == '#' and m[y+1][x] == '#' and m[y][x] == '#' and m[y][x-1] == '#' and m[y][x+1] == '#':
            s += x*y
print(s)
