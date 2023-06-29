#!/usr/bin/env python3
import sys
from intcode import *
text = parsetext(input())
vms = [IntcodeVM(text.copy(), [i]) for i in range(50)]
nat = (None, None)
lastnat = (None, None)
while True:
    idle = True
    for vm in vms:
        if len(vm.inq) == 0:
            vm.inq.append(-1)
        else:
            idle = False
        vm.run()
        while len(vm.outq):
            idle = False
            d, x, y = vm.outq[:3]
            del vm.outq[:3]
            if d == 255:
                nat = (x, y)
            else:
                vms[d].inq += (x, y)
    if idle:
        if nat[1] == lastnat[1]:
            print(nat[1])
            sys.exit(0)
        vms[0].inq += nat
        lastnat = nat
