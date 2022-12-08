#!/usr/bin/env python3
import sys
insns = list(map(lambda x: x.split(), sys.stdin.read().splitlines()))
pc = 0
regs = {'a': 0, 'b': 0}
while pc < len(insns):
    insn = insns[pc]
    if insn[0] == 'hlf':
        regs[insn[1]] //= 2
        pc += 1
    elif insn[0] == 'tpl':
        regs[insn[1]] *= 3
        pc += 1
    elif insn[0] == 'inc':
        regs[insn[1]] += 1
        pc += 1
    elif insn[0] == 'jmp':
        pc += int(insn[1])
    elif insn[0] == 'jie':
        pc += int(insn[2]) if regs[insn[1][0]]%2 == 0 else 1
    elif insn[0] == 'jio':
        pc += int(insn[2]) if regs[insn[1][0]] == 1 else 1
print(regs['b'])
