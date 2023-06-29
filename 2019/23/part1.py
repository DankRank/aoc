#!/usr/bin/env python3
import sys
from intcode import *
text = parsetext(input())
vms = [IntcodeVM(text.copy(), [i]) for i in range(50)]
while True:
    for vm in vms:
        if len(vm.inq) == 0:
            vm.inq.append(-1)
        vm.run()
        while len(vm.outq):
            d, x, y = vm.outq[:3]
            del vm.outq[:3]
            if d == 255:
                print(y)
                sys.exit(0)
            vms[d].inq += (x, y)
