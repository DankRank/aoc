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
def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
m = {}
vm = IntcodeVM(text.copy())
vm.text[0] = 2
score = 0
while not vm.halted:
    vm.run()
    while len(vm.outq):
        x = vm.outq.pop(0)
        y = vm.outq.pop(0)
        v = vm.outq.pop(0)
        if x == -1 and y == 0:
            score = v
        else:
            if v == 3:
                paddlex = x
            elif v == 4:
                ballx = x
            m[(x,y)] = v
    #minx = min(m.keys(), key=lambda x: x[0])[0]
    #maxx = max(m.keys(), key=lambda x: x[0])[0]
    #miny = min(m.keys(), key=lambda x: x[1])[1]
    #maxy = max(m.keys(), key=lambda x: x[1])[1]
    #print('\033[H')
    #for y in range(miny, maxy+1):
    #    line = []
    #    for x in range(minx, maxx+1):
    #        line.append(str(m[(x,y)]))
    #    print(''.join(line))
    #print(score)
    vm.inq.append(int(sgn(ballx-paddlex)))
print(score)
