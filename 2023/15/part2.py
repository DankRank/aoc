#!/usr/bin/env python3
def hash(s):
    h = 0
    for ch in s:
        h = ((h+ord(ch))*17)&255
    return h
boxes = [[] for i in range(256)]
m = {}
for s in input().split(','):
    if s[-1] == '-':
        l = s[:-1]
        box = boxes[hash(l)]
        if l in m:
            del box[m[l]]
            for i in range(m[l], len(box)):
                m[box[i][0]] -= 1
            del m[l]
    else:
        l = s[:-2]
        box = boxes[hash(l)]
        if l in m:
            box[m[l]] = (l, int(s[-1]))
        else:
            m[l] = len(box)
            box.append((l, int(s[-1])))
print(sum((i+1)*(j+1)*k[1] for i, box in enumerate(boxes) for j, k in enumerate(box)))
