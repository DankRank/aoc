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
vm = IntcodeVM(text.copy())
vm.text[0] = 2
vm.run()
m = ['.'+x+'.' for x in ''.join(chr(x) for x in vm.outq).split()]
del m[-1]
m.insert(0, '.'*len(m[0]))
m.append('.'*len(m[0]))
scaffolds = set()
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] not in '.#':
            if m[i][j] == '^':
                dx, dy = 0, -1
            elif m[i][j] == 'V':
                dx, dy = 0, 1
            elif m[i][j] == '<':
                dx, dy = -1, 0
            elif m[i][j] == '>':
                dx, dy = 1, 0
            else:
                raise ValueError(f'what\'s {m[i][j]}')
            x, y = j, i
        if m[i][j] != '.':
            scaffolds.add((j, i))
path = []
fwd = 0
while True:
    while (x+dx, y+dy) in scaffolds:
        x += dx
        y += dy
        fwd += 1
    if fwd:
        path.append(str(fwd))
        fwd = 0
    # turn left: y, -x
    # turn right: -y, x
    if (x+dy, y-dx) in scaffolds:
        path.append('L')
        dx, dy = dy, -dx
    elif (x-dy, y+dx) in scaffolds:
        path.append('R')
        dx, dy = -dy, dx
    else:
        break
progs = []
main = []
# educated guess
for i in [8, 8, 8, 6, 8, 8, 6, 8, 6, 8]:
    # print(path[:i])
    try:
        idx = progs.index(path[:i])
    except ValueError:
        idx = len(progs)
        progs.append(path[:i])
    main.append(chr(65+idx))
    path = path[i:]
vm.outq = []
vm.inq += ''.join(','.join(line)+'\n' for line in [main, *progs, ['n']]).encode()
vm.run()
print(vm.outq[-1])
