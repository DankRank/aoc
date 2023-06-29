#!/usr/bin/env python3
import sys
import functools
from intcode import *
text = parsetext(input())
@functools.cache
def probe(x, y):
    if x < 0 or y < 0:
        return 0
    vm = IntcodeVM(text.copy(), [x, y])
    vm.run()
    return vm.outq[0]
print(sum(probe(x, y) for y in range(50) for x in range(50)))

x, y = 0, 0
while True:
    while not probe(x, y):
        x += 1
    while probe(x, y):
        if probe(x-99, y+99):
            print((x-99)*10000+y)
            sys.exit(0)
        x += 1
    x -= 1
    y += 1
