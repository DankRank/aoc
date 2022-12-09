#!/usr/bin/env python3
import sys
insns = list(map(lambda x: x.split(), sys.stdin.read().splitlines()))
pc = 0
regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
def getval(v):
    return regs[v] if v in regs else int(v)
while pc < len(insns):
    insn = insns[pc]
    if insn[0] == 'cpy':
        regs[insn[2]] = getval(insn[1])
        pc += 1
    elif insn[0] == 'inc':
        regs[insn[1]] += 1
        pc += 1
    elif insn[0] == 'dec':
        regs[insn[1]] -= 1
        pc += 1
    elif insn[0] == 'jnz':
        pc += int(insn[2]) if getval(insn[1]) != 0 else 1
print(regs['a'])
