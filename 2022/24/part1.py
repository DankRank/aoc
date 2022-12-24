#!/usr/bin/env python3
import sys
lines = sys.stdin.read().splitlines()
up    = set((x-1, y-1) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '^')
down  = set((x-1, y-1) for y, line in enumerate(lines) for x, c in enumerate(line) if c == 'v')
left  = set((x-1, y-1) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '<')
right = set((x-1, y-1) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '>')
w = len(lines[0])-2
h = len(lines)-2
start_pos = (0, -1)
end_pos = (w-1, h)
def valid_pos(p):
    return p == start_pos or p == end_pos or p[0] >= 0 and p[1] >= 0 and p[0] < w and p[1] < h
def collides_on_step(p, s):
    return (not valid_pos(p) or
            ((p[0]-s)%w, p[1]) in right or
            ((p[0]+s)%w, p[1]) in left or
            (p[0], (p[1]-s)%h) in down or
            (p[0], (p[1]+s)%h) in up)
def gen_moves(p):
    yield p[0], p[1]
    yield p[0]-1, p[1]
    yield p[0]+1, p[1]
    yield p[0], p[1]-1
    yield p[0], p[1]+1
prev_states = set()
next_states = {start_pos}
step = 0
while end_pos not in next_states:
    prev_states, next_states = next_states, set()
    step += 1
    for p in prev_states:
        for p in gen_moves(p):
            if not collides_on_step(p, step):
                next_states.add(p)
print(step)
