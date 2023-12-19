#!/usr/bin/env python3
workflows = {}
items = []
try:
    while True:
        line = input()
        if line == '':
            break
        label, line = line.rstrip('}').split('{')
        line = line.split(',')
        workflow = []
        for i, rule in enumerate(line[:-1]):
            cond, then = rule.split(':')
            lhs = 'xmas'.index(cond[0])
            gt = cond[1] == '>'
            rhs = int(cond[2:])
            workflow.append((lhs, gt, rhs, then))
        workflow.append(line[-1])
        workflows[label] = workflow
    while True:
        items.append([int(c.split('=')[1]) for c in input().strip('{}').split(',')])
except EOFError:
    pass

s = 0
for item in items:
    label = 'in'
    while label not in ('A', 'R'):
        for lhs, gt, rhs, then in workflows[label][:-1]:
            if (item[lhs] > rhs) if gt else (item[lhs] < rhs):
                label = then
                break
        else:
            label = workflows[label][-1]
    if label == 'A':
        s += sum(item)
print(s)
