#!/usr/bin/env python3
import sys
mapp = [list(line) for line in sys.stdin.read().splitlines()]
for r, line in enumerate(mapp):
    for c, ch in enumerate(line):
        if ch == 'S':
            init_state = (r, c)
            ch = 'a'
        elif ch == 'E':
            fini_state = (r, c)
            ch = 'z'
        mapp[r][c] = ord(ch) - ord('a')

known_states = {init_state}
prev_states = set()
next_states = {init_state}
generation = 0
def neighbors(s):
    r, c = s
    if r > 0:
        yield (r-1, c)
    if r < len(mapp)-1:
        yield (r+1, c)
    if c > 0:
        yield (r, c-1)
    if c < len(mapp[0])-1:
        yield (r, c+1)
while fini_state not in known_states:
    prev_states, next_states = next_states, set()
    generation += 1
    assert len(prev_states) > 0
    for s in prev_states:
        for ns in neighbors(s):
            if mapp[ns[0]][ns[1]] <= mapp[s[0]][s[1]]+1:
                if ns not in known_states:
                    known_states.add(ns)
                    next_states.add(ns)
print(generation)
