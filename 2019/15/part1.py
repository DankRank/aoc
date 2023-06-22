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
visited = {(0, 0)}
walls = set()
oxygen = None
x, y = 0, 0
stack = [4, 3, 2, 1]
inverse = [None, 2, 1, 4, 3]
while len(stack):
    d = stack.pop()
    backtracking = d < 0
    if backtracking:
        d = inverse[-d]
    if d == 1:
        nx, ny = x, y-1
    elif d == 2:
        nx, ny = x, y+1
    elif d == 3:
        nx, ny = x-1, y
    elif d == 4:      
        nx, ny = x+1, y
    if not backtracking and (nx, ny) in visited:
        continue
    vm.inq.append(d)
    vm.run()
    r = vm.outq.pop(0)
    if r == 0:
        walls.add((nx, ny))
    else:
        if r == 2:
            oxygen = (nx, ny)
        x, y = nx, ny
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            stack += [-d, 4, 3, 2, 1]
assert oxygen is not None

generation = 0
known_states = {(0, 0)} | walls
next_states = {(0, 0)}
prev_states = set()
while oxygen not in known_states:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for x, y in prev_states:
        for ns in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            if ns not in known_states:
                next_states.add(ns)
                known_states.add(ns)
print(generation)

target = len(walls) + len(visited)
generation = 0
known_states = {oxygen} | walls
next_states = {oxygen}
prev_states = set()
while len(known_states) != target:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for x, y in prev_states:
        for ns in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            if ns not in known_states:
                next_states.add(ns)
                known_states.add(ns)
print(generation)
