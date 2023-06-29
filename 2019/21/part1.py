#!/usr/bin/env python3
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
