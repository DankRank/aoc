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
    corrected = False
    while True:
        right = set(update)
        assert(len(right) == len(update)) # this better be unique
        for i in range(len(update)):
            right.remove(update[i])
            if before[update[i]] & right:
                corrected = True
                for j in range(len(update)-1, i, -1):
                    if update[j] in before[update[i]]:
                        update[i], update[j] = update[j], update[i]
                        break
                break # out of order, try again
        else:
            if corrected:
                count += update[len(update)//2]
            break
print(count)
