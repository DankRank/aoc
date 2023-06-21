#!/usr/bin/env python3
import itertools
text = [int(line) for line in input().split(',')]
def intcode(text, inq):
    outq = []
    pc = 0
    def fetch(addr, mode):
        if mode == 0:
            return text[addr]
        elif mode == 1:
            return addr
        else:
            raise ValueError(f'unknown mode {mode}')
    while True:
        op = text[pc]%100
        amode = text[pc]//100%10
        bmode = text[pc]//1000%10
        cmode = text[pc]//10000%10
        if op == 1:
            text[text[pc+3]] = fetch(text[pc+1], amode) + fetch(text[pc+2], bmode)
            pc += 4
        elif op == 2:
            text[text[pc+3]] = fetch(text[pc+1], amode) * fetch(text[pc+2], bmode)
            pc += 4
        elif op == 3:
            text[text[pc+1]] = inq.pop(0)
            pc += 2
        elif op == 4:
            outq.append(fetch(text[pc+1], amode))
            pc += 2
        elif op == 5:
            pc = fetch(text[pc+2], bmode) if fetch(text[pc+1], amode) != 0 else pc+3
        elif op == 6:
            pc = fetch(text[pc+2], bmode) if fetch(text[pc+1], amode) == 0 else pc+3
        elif op == 7:
            text[text[pc+3]] = int(fetch(text[pc+1], amode) < fetch(text[pc+2], bmode))
            pc += 4
        elif op == 8:
            text[text[pc+3]] = int(fetch(text[pc+1], amode) == fetch(text[pc+2], bmode))
            pc += 4
        elif op == 99:
            break
        else:
            raise ValueError(f'unknown op {op} at {pc}')
    return outq
res = 0
for a, b, c, d, e in itertools.permutations(range(5)):
    q = intcode(text.copy(), [a, 0])
    q = intcode(text.copy(), [b, q[0]])
    q = intcode(text.copy(), [c, q[0]])
    q = intcode(text.copy(), [d, q[0]])
    q = intcode(text.copy(), [e, q[0]])
    res = max(res, q[0])
print(res)
