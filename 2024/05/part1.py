#!/usr/bin/env python3
order = []
updates = []
try:
    while True:
        line = input()
        if line == '':
            break
        order.append(tuple(int(x) for x in line.split('|')))
    while True:
        updates.append([int(x) for x in input().split(',')])
except EOFError:
    pass

before = {i:set() for i in range(100)}
for a, b in order:
    before[b].add(a)

count = 0
for update in updates:
    right = set(update)
    assert(len(right) == len(update)) # this better be unique
    for i in range(len(update)):
        right.remove(update[i])
        if before[update[i]] & right:
            break # out of order
    else:
        count += update[len(update)//2]
print(count)
