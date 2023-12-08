#!/usr/bin/env python3
path = input()
m = {}
input()
try:
    while True:
        k, v = input().rstrip(')').split(' = (')
        m[k] = v.split(', ')
except EOFError:
    pass

steps = 0
node = 'AAA'
while node != 'ZZZ':
    for i in path:
        node = m[node][int(i == 'R')]
        steps += 1
        if node == 'ZZZ':
            break
print(steps)
