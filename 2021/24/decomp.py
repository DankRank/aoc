#!/usr/bin/env python3
def dumpExpr(expr, prec=0):
    if isinstance(expr, list):
        if expr[0] == 'inp':
            return 'in['+str(expr[1])+']'
        elif expr[0] == 'add':
            s = dumpExpr(expr[1]) + ' + ' + dumpExpr(expr[2])
            return '('+s+')' if prec > 0 else s
        elif expr[0] == 'mul':
            s = dumpExpr(expr[1], 2) + '*' + dumpExpr(expr[2], 1)
            return '('+s+')' if prec > 1 else s
        elif expr[0] == 'div':
            s = dumpExpr(expr[1], 2) + '/' + dumpExpr(expr[2], 1)
            return '('+s+')' if prec > 1 else s
        elif expr[0] == 'mod':
            s = dumpExpr(expr[1], 2) + '%' + dumpExpr(expr[2], 1)
            return '('+s+')' if prec > 1 else s
        elif expr[0] == 'eql':
            return 'eq(' + dumpExpr(expr[1]) + ', ' + dumpExpr(expr[2]) + ')'
        elif expr[0] == 'neq':
            return 'neq(' + dumpExpr(expr[1]) + ', ' + dumpExpr(expr[2]) + ')'
    else:
        return str(expr)

regs = {
    'w': 'w0',
    'x': 'x0',
    'y': 'y0',
    'z': 'z0'
}

inp_count = 0
try:
    while True:
        insn = input().split()
        if insn[0] == 'inp':
            regs[insn[1]] = ['inp', inp_count]
            inp_count += 1
        else:
            regs[insn[1]] = [insn[0], regs[insn[1]], regs[insn[2]] if insn[2] in regs else int(insn[2])]
except EOFError:
    pass

def maplists(fn, expr):
    repcnt = 0
    for i in range(len(expr)):
        if isinstance(expr[i], list):
            rep = fn(expr[i])
            if rep is None:
                repcnt += maplists(fn, expr[i])
            elif rep is not False:
                expr[i] = rep
                repcnt += 1
    return repcnt

simplify_seen = {}
def simplify(expr):
    if id(expr) in simplify_seen:
        return False
    else:
        simplify_seen[id(expr)] = expr
    if expr[0] == 'add':
        if expr[1] == 0:
            return expr[2]
        if expr[2] == 0:
            return expr[1]
    elif expr[0] == 'mul':
        if expr[1] == 0 or expr[2] == 0:
            return 0
        if expr[1] == 1:
            return expr[2]
        if expr[2] == 1:
            return expr[1]
    elif expr[0] == 'div':
        if expr[1] == 0:
            return 0
        if expr[2] == 1:
            return expr[1]
    elif expr[0] == 'mod':
        if expr[1] == 0:
            return 0
        if expr[2] == 1:
            return 0
    elif expr[0] == 'eql':
        if not isinstance(expr[1], list) and not isinstance(expr[2], list):
            return 1 if expr[1] == expr[2] else 0
        else:
            if expr[1] == 0 and expr[2][0] == 'eql':
                return ['neq', expr[2][1], expr[2][2]]
            if expr[2] == 0 and expr[1][0] == 'eql':
                return ['neq', expr[1][1], expr[1][2]]
while maplists(simplify, regs['z']) > 0:
    simplify_seen = {}

known_exprs1 = {}
known_exprs2 = {}
def learn(expr):
    if id(expr) in known_exprs1:
        known_exprs2[id(expr)] = expr
        return False
    else:
        known_exprs1[id(expr)] = expr
maplists(learn, regs['z'])

names = {}
lastname = 0
for i, expr in known_exprs2.items():
    if expr[0] == 'inp':
        names[i] = 'inp['+str(expr[1])+']'
    else:
        names[i] = 'a'+str(lastname)
        lastname += 1
def rename(expr):
    if id(expr) in names:
        return names[id(expr)]
for expr in known_exprs2.values():
    maplists(rename, expr)
maplists(rename, regs['z'])

for i in names:
    if not names[i].startswith('inp'):
        print(names[i] + ' = ' + dumpExpr(known_exprs2[i]))
print('z = ' + dumpExpr(regs['z']))
