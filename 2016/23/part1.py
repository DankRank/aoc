#!/usr/bin/env python3
import sys
insns = list(map(lambda x: x.split(), sys.stdin.read().splitlines()))
pc = 0
regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
def getval(v):
    return regs[v] if v in regs else int(v)
while pc < len(insns):
    insn = insns[pc]
    if insn[0] == 'cpy':
        if insn[2] in regs:
            regs[insn[2]] = getval(insn[1])
        pc += 1
    elif insn[0] == 'inc':
        if insn[1] in regs:
            regs[insn[1]] += 1
        pc += 1
    elif insn[0] == 'dec':
        if insn[1] in regs:
            regs[insn[1]] -= 1
        pc += 1
    elif insn[0] == 'jnz':
        pc += getval(insn[2]) if getval(insn[1]) != 0 else 1
    elif insn[0] == 'tgl':
        ptr = pc + getval(insn[1])
        if ptr >= 0 and ptr < len(insns):
            p = insns[ptr]
            if len(p) == 2:
                p[0] = 'dec' if p[0] == 'inc' else 'inc'
            else:
                p[0] = 'cpy' if p[0] == 'jnz' else 'jnz'
        pc += 1
print(regs['a'])
