#!/usr/bin/env python3
regs = [int(input().split(': ')[1]) for i in range(3)]
input()
program = [int(x) for x in input().split(': ')[1].split(',')]

ip = 0
def getliteral():
    return program[ip+1]
def getcombo():
    i = program[ip+1]
    if i < 4:
        return i
    else:
        return regs[i-4]

output = []
while ip < len(program):
    if program[ip] == 0: # adv
        regs[0] //= 1<<getcombo()
    elif program[ip] == 1: # bxl
        regs[1] ^= getliteral()
    elif program[ip] == 2: # bst
        regs[1] = getcombo()&7
    elif program[ip] == 3: # jnz
        if regs[0]:
            ip = getliteral()-2
    elif program[ip] == 4: # bxc
        regs[1] ^= regs[2]
    elif program[ip] == 5: # out
        output.append(getcombo()&7)
    elif program[ip] == 6: # bdv
        regs[1] = regs[0] // (1<<getcombo())
    elif program[ip] == 7: # cdv
        regs[2] = regs[0] // (1<<getcombo())
    ip += 2

print(','.join(str(x) for x in output))
