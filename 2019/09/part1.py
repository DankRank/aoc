#!/usr/bin/env python3
from intcode import *
text = parsetext(input())
vm = IntcodeVM(text.copy(), [1])
vm.run()
print(vm.outq[0])
vm = IntcodeVM(text.copy(), [2])
vm.run()
print(vm.outq[0])
