#!/usr/bin/env python3
W, H = 38, 26
import bisect
input()
input()
totals = []
init_state = []
try:
    while True:
        t, u = (int(s.rstrip('T')) for s in input().split()[1:3])
        totals.append(t)
        init_state.append(u)
except EOFError:
    pass
init_state.append((W-1)*H)
init_state.append(0)
init_state = tuple(init_state)
assert len(init_state) == W*H + 2

def neighbors(x, y):
    if x < W-1:
        yield (x+1)*H+y
    if x > 0:
        yield (x-1)*H+y
    if y < H-1:
        yield x*H+y+1
    if y > 0:
        yield x*H+y-1

known_states = set()
next_states = {init_state}
prev_states = set()
generation = 0
found = False
while not found:
    prev_states, next_states = next_states, set()
    assert len(prev_states) > 0
    for s in prev_states:
        for x in range(W):
            for y in range(H):
                i = x*H+y
                if s[i] > 0:
                    for j in neighbors(x, y):
                        if s[i] + s[j] <= totals[j]:
                            ns = list(s)
                            ns[j] += ns[i]
                            ns[i] = 0
                            if ns[W*H] == i:
                                ns[W*H] = j
                                if j == 0:
                                    found = True
                                ns[W*H+1] += 1
                            ns = tuple(ns)
                            if ns not in known_states:
                                known_states.add(ns)
                            next_states.add(ns)
    generation += 1
    print(generation)
print(generation)
