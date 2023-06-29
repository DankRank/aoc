#!/usr/bin/env python3
import sys
text = [int(line) for line in input().split(',')]
class IntcodeVM:
    __slots__ = 'text', 'pc', 'relbase', 'inq', 'outq', 'halted'
    def __init__(self, text, inq = []):
        self.text = text
        self.pc = 0
        self.relbase = 0
        self.inq = inq
        self.outq = []
        self.halted = False
    def checkaddr(self, addr):
        if addr >= len(self.text):
            self.text += [0]*(addr+1-len(self.text))
    def fetch(self, addr):
        self.checkaddr(addr)
        return self.text[addr]
    def store(self, addr, val):
        self.checkaddr(addr)
        self.text[addr] = val
    def arg(self, idx):
        addr = self.fetch(self.pc+idx)
        mode = self.fetch(self.pc)//10**(idx+1)%10
        if mode == 0:
            return self.fetch(addr)
        elif mode == 1:
            return addr
        elif mode == 2:
            return self.fetch(self.relbase+addr)
        else:
            raise ValueError(f'unknown mode {mode}')
    def argwr(self, idx, val):
        addr = self.fetch(self.pc+idx)
        mode = self.fetch(self.pc)//10**(idx+1)%10
        if mode == 0:
            self.store(addr, val)
        elif mode == 2:
            self.store(self.relbase+addr, val)
        else:
            raise ValueError(f'unknown mode {mode}')
    def step(self):
        op = self.fetch(self.pc)%100
        if op == 1:
            self.argwr(3, self.arg(1) + self.arg(2))
            self.pc += 4
        elif op == 2:
            self.argwr(3, self.arg(1) * self.arg(2))
            self.pc += 4
        elif op == 3:
            if not len(self.inq):
                return False
            self.argwr(1, self.inq.pop(0))
            self.pc += 2
        elif op == 4:
            self.outq.append(self.arg(1))
            self.pc += 2
        elif op == 5:
            self.pc = self.arg(2) if self.arg(1) != 0 else self.pc+3
        elif op == 6:
            self.pc = self.arg(2) if self.arg(1) == 0 else self.pc+3
        elif op == 7:
            self.argwr(3, int(self.arg(1) < self.arg(2)))
            self.pc += 4
        elif op == 8:
            self.argwr(3, int(self.arg(1) == self.arg(2)))
            self.pc += 4
        elif op == 9:
            self.relbase += self.arg(1)
            self.pc += 2
        elif op == 99:
            self.halted = True
            return False
        else:
            raise ValueError(f'unknown op {op} at {pc}')
        return True
    def run(self):
        while self.step():
            pass
vm = IntcodeVM(text.copy())
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
