#!/usr/bin/env python3
text = [int(line) for line in input().split(',')]
class IntcodeVM:
    __slots__ = 'text', 'pc'
    def __init__(self, text):
        self.text = text
        self.pc = 0
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
            self.argwr(1, int(input()))
            self.pc += 2
        elif op == 4:
            print(self.arg(1))
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
            return False
        else:
            raise ValueError(f'unknown op {op} at {self.pc}')
        return True
    def run(self):
        while self.step():
            pass
IntcodeVM(text).run()
