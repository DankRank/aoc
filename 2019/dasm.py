#!/usr/bin/python3
import sys
if len(sys.argv) < 3:
    print('Usage: dasm.py input.txt db.txt')
    sys.exit(0)

labels = {}
refs = {}
info = {}

with open(sys.argv[1]) as f:
    text = [int(x) for x in f.readline().rstrip().split(',')]
with open(sys.argv[2]) as f:
    for line in f:
        line = line.rstrip().split('#')[0].split()
        if not len(line):
            continue
        if line[0] == 'label':
            labels[int(line[1])] = line[2]
        elif line[0] == 'ref':
            refs[int(line[1])] = line[2]
        elif line[0] in ('text', 'number', 'ascii'):
            for i in range(int(line[1]), int(line[2])+1):
                if i in info:
                    raise ValueError(f'{line} : {i} is already known')
                info[i] = line[0]
        else:
            raise ValueError(f'what is a {line[1]}')
def renderref(pc):
    if pc not in refs:
        if text[pc] in labels:
            return labels[text[pc]]
        return str(text[pc])
    elif refs[pc] == 'ascii':
        return chr(text[pc])
    elif refs[pc] == 'data':
        return str(text[pc])
    else:
        raise ValueError(f'unknown ref: {pc} {refs[pc]}')
def renderarg(pc, idx, wr=False):
    mode = text[pc]//10**(idx+1)%10
    if mode < 0 or mode > 2 or (wr and mode == 1):
        raise ValueError(f'unknown mode {mode} @ {pc}')
    return ['$','','@'][mode]+renderref(pc+idx)
def renderinsn(pc):
    op = text[pc]%100
    if op == 1:
        return 4, f'    add {renderarg(pc,1)} {renderarg(pc,2)} {renderarg(pc,3,True)}'
    elif op == 2:
        return 4, f'    mul {renderarg(pc,1)} {renderarg(pc,2)} {renderarg(pc,3,True)}'
    elif op == 3:
        return 2, f'    inp {renderarg(pc,1,True)}'
    elif op == 4:
        return 2, f'    out {renderarg(pc,1)}'
    elif op == 5:
        return 3, f'    jnz {renderarg(pc,1)} {renderarg(pc,2)}'
    elif op == 6:
        return 3, f'    jz  {renderarg(pc,1)} {renderarg(pc,2)}'
    elif op == 7:
        return 4, f'    slt {renderarg(pc,1)} {renderarg(pc,2)} {renderarg(pc,3,True)}'
    elif op == 8:
        return 4, f'    seq {renderarg(pc,1)} {renderarg(pc,2)} {renderarg(pc,3,True)}'
    elif op == 9:
        return 2, f'    rel {renderarg(pc,1)}'
    elif op == 99:
        return 1, f'    hlt'
    else:
        raise ValueError(f'unknown op {op} at {pc}')
def rendersuffix(pc, adv, line):
    line += ' '*(60-len(line))
    line += f'; {pc}: '
    line += ' '.join(str(text[x]) for x in range(pc,pc+adv))
    if any(x not in info for x in range(pc, pc+adv)):
        line += ' UNMARKED'
    return line
lastinfo = 'text'
pc = 0
while pc < len(text):
    if pc in labels:
        print(f'{labels[pc]}:')
    if pc in info:
        lastinfo = info[pc]
    if lastinfo == 'text':
        try:
            adv, line = renderinsn(pc)
        except (ValueError, IndexError):
            if pc in info: raise
            lastinfo = 'number'
            adv, line = 1, f'    num {renderref(pc)}'
    elif lastinfo == 'number' or lastinfo == 'ascii':
        adv, line = 1, f'    num {renderref(pc)}'
    print(rendersuffix(pc, adv, line))
    pc += adv

