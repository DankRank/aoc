#!/usr/bin/env python3
workflows = {}
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
        input()
except EOFError:
    pass

s = 0
st = [([range(1,4001)]*4, 'in', 0)]
while len(st):
    item, label, i = st.pop()
    if label == 'A':
        s += len(item[0]) * len(item[1]) * len(item[2]) * len(item[3]) 
    elif label == 'R':
        pass
    elif i == len(workflows[label])-1:
        st.append((item, workflows[label][-1], 0))
    else:
        lhs, gt, rhs, then = workflows[label][i]
        if gt:
            if item[lhs].start > rhs:
                st.append((item, then, 0))
            elif item[lhs].stop-1 <= rhs:
                st.append((item, label, i+1))
            else:
                copy = item.copy()
                copy[lhs] = range(rhs+1, copy[lhs].stop)
                st.append((copy, then, 0))
                item[lhs] = range(item[lhs].start, rhs+1)
                st.append((item, label, i+1))
        else:
            if item[lhs].stop-1 < rhs:
                st.append((item, then, 0))
            elif item[lhs].start >= rhs:
                st.append((item, label, i+1))
            else:
                copy = item.copy()
                copy[lhs] = range(copy[lhs].start, rhs)
                st.append((copy, then, 0))
                item[lhs] = range(rhs, item[lhs].stop)
                st.append((item, label, i+1))
print(s)
