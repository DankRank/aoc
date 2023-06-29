#!/usr/bin/env python3
from intcode import *
vm = IntcodeVM(parsetext(input()))
visited = {(0, 0)}
walls = set()
oxygen = None
x, y = 0, 0
stack = [4, 3, 2, 1]
inverse = [None, 2, 1, 4, 3]
while len(stack):
    d = stack.pop()
    backtracking = d < 0
    if backtracking:
        d = inverse[-d]
    if d == 1:
        nx, ny = x, y-1
    elif d == 2:
        nx, ny = x, y+1
    elif d == 3:
        nx, ny = x-1, y
    elif d == 4:      
        nx, ny = x+1, y
    if not backtracking and (nx, ny) in visited:
        continue
    vm.inq.append(d)
    vm.run()
    r = vm.outq.pop(0)
    if r == 0:
        walls.add((nx, ny))
    else:
        if r == 2:
            oxygen = (nx, ny)
        x, y = nx, ny
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            stack += [-d, 4, 3, 2, 1]
assert oxygen is not None

generation = 0
known_states = {(0, 0)} | walls
next_states = {(0, 0)}
prev_states = set()
while oxygen not in known_states:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for x, y in prev_states:
        for ns in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            if ns not in known_states:
                next_states.add(ns)
                known_states.add(ns)
print(generation)

target = len(walls) + len(visited)
generation = 0
known_states = {oxygen} | walls
next_states = {oxygen}
prev_states = set()
while len(known_states) != target:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for x, y in prev_states:
        for ns in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
            if ns not in known_states:
                next_states.add(ns)
                known_states.add(ns)
print(generation)
