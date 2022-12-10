#!/usr/bin/env python3
import functools
constant = int(input())
@functools.cache
def readmap(x, y):
    if x < 0 or y < 0:
        return 1
    return sum(1 for i in bin(x*x + 3*x + 2*x*y + y + y*y + constant) if i == '1')%2
init_state = (1,1)
fini_state = (31,39)
visited = {init_state}
next_states = {init_state}
prev_states = set()
generation = 0
while fini_state not in visited:
    generation += 1
    prev_states, next_states = next_states, set()
    for x, y in prev_states:
        for x, y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if readmap(x, y) == 0:
                visited.add((x, y))
                next_states.add((x, y))
print(generation)
