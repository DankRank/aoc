#!/usr/bin/env python3
line = [int(x) for x in input()]
assert len(line) % 2
i = 0
j = len(line)-1
newrle = []
while i < j:
    if i%2 == 0:
        if line[i]:
            newrle.append((i//2, line[i]))
        i += 1
    else:
        while line[i] and i < j:
            diff = min(line[i], line[j])
            line[i] -= diff
            line[j] -= diff
            if diff:
                newrle.append((j//2, diff))
            while not line[j]:
                j -= 2
        i += 1
if i == j and line[i]:
    newrle.append((i//2, line[i]))
count = 0
pos = 0
for fileid, rep in newrle:
    count += fileid*(pos*rep + rep*(rep-1)//2)
    pos += rep
print(count)
