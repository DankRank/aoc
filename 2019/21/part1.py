#!/usr/bin/env python3
from intcode import *
text = parsetext(input())
prog1 = '''\
NOT J J
AND C J
AND B J
AND A J
NOT J J
AND D J
WALK
'''
vm = IntcodeVM(text.copy(), [ord(x) for x in prog1])
vm.run()
#print(''.join(chr(x) for x in vm.outq if x < 128))
print(vm.outq[-1])

prog2 = '''\
NOT J J
AND C J
AND B J
AND A J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN
'''
vm = IntcodeVM(text.copy(), [ord(x) for x in prog2])
vm.run()
#print(''.join(chr(x) for x in vm.outq if x < 128))
print(vm.outq[-1])
