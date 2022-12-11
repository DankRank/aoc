#!/usr/bin/env python3
W, H = 38, 26
input()
input()
mapp = [1]*(H+1)
for i in range(W):
    mapp.append(1)
    for j in range(H):
        u = int(input().split()[2].rstrip('T'))
        if u == 0:
            empty_cell = len(mapp)
        mapp.append(1 if u > 100 else 0)
mapp += [1]*(H+2)
init_state = (empty_cell, (H+1)*W+1)

#def print_state(s):
#    p, q = s
#    for i in range(0, W+2):
#        st = ''
#        for j in range((H+1)*i, (H+1)*(i+1)+1):
#            st += '_' if j == p else 'G' if j == q else '#' if mapp[j] else '.'
#        print(st)

def neighbors(p):
    if mapp[p-H-1] == 0:
        yield p-H-1
    if mapp[p+H+1] == 0:
        yield p+H+1
    if mapp[p-1] == 0:
        yield p-1
    if mapp[p+1] == 0:
        yield p+1

known_states = set()
next_states = {init_state}
prev_states = set()
generation = 0
found = False
while not found:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for p, q in prev_states:
        for i in neighbors(p):
            if i == q:
                s = (q, p)
                if p == H+1+1:
                    found = True
            else:
                s = (i, q)
            if s not in known_states:
                known_states.add(s)
                next_states.add(s)
print(generation)
