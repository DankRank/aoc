#!/usr/bin/env python3
import itertools
text = [int(line) for line in input().split(',')]
class IntcodeVM:
    __slots__ = 'text', 'pc', 'inq', 'outq', 'halted'
    def __init__(self, text, inq = []):
        self.text = text
        self.pc = 0
        self.inq = inq
        self.outq = []
        self.halted = False
    def fetch(self, addr, mode):
        if mode == 0:
            return self.text[addr]
        elif mode == 1:
            return addr
        else:
            raise ValueError(f'unknown mode {mode}')
    def arg(self, idx):
        return self.fetch(self.text[self.pc+idx], self.text[self.pc]//10**(idx+1)%10)
    def argwr(self, idx, val):
        self.text[self.text[self.pc+idx]] = val
    def step(self):
        op = self.text[self.pc]%100
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
        elif op == 99:
            self.halted = True
            return False
        else:
            raise ValueError(f'unknown op {op} at {pc}')
        return True
    def run(self):
        while self.step():
            pass
res = 0
for p in itertools.permutations(range(5, 10)):
    vms = [IntcodeVM(text.copy(), [a]) for a in p]
    buf = [0]
    while not vms[-1].halted:
        for vm in vms:
            vm.inq += buf
            vm.run()
            buf = vm.outq
            vm.outq = []
    res = max(res, buf[-1])
print(res)
