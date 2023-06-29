#!/usr/bin/env python3
import sys
from intcode import *
vm = IntcodeVM(parsetext(input()))
def runvm(line):
    vm.inq = [ord(x) for x in line]
    vm.run()
    out = ''.join(chr(x) for x in vm.outq)
    vm.outq = []
    return line+out
if len(sys.argv) > 1 and sys.argv[1] == '-i':
    line = ''
    while True:
        print(runvm(line), end='')
        if vm.halted:
            break
        line = input()+'\n'
        if line == 'do a trick\n':
            items = ['astrolabe', 'bowl of rice', 'fuel cell', 'hologram', 'monolith', 'mug', 'ornament', 'weather machine']
            itemsmap = {1<<k:v for k, v in enumerate(items)}
            print('TRYING 0 ' + ', '.join(items))
            print(runvm('north\n'), end='')
            for i in range(1, 256):
                gray = i ^ i>>1
                diff = (i-1) ^ (i-1)>>1 ^ gray
                action = 'drop' if diff & gray else 'take'
                print(f'TRYING {i} ' + ', '.join(x for i, x in enumerate(items) if gray & 1<<i == 0))
                print(runvm(f'{action} {itemsmap[diff]}\nnorth\n'), end='')
            line = ''
else:
    tas = '''\
west
west
south
take hologram
north
north
take fuel cell
south
take astrolabe
east
take ornament
east
east
south
west
north
west
north
west
north
'''
    print(''.join(x for x in runvm(tas).splitlines()[-1] if x.isdigit()))
