#!/usr/bin/env python3
from intcode import *
m = {}
vm = IntcodeVM(parsetext(input()))
vm.run()
while len(vm.outq):
    x = vm.outq.pop(0)
    y = vm.outq.pop(0)
    v = vm.outq.pop(0)
    m[(x,y)] = v
print(sum(1 for v in m.values() if v == 2))
