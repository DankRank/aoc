#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def neighbors(s):
    if s[1] == 0:
        yield (s[0], s[1]+1)
    else:
        i = '>^<v'.find(m[s[1]][s[0]])
        if i == -1:
            for i in range(4):
                ns = (s[0]+dirs[i][0], s[1]+dirs[i][1])
                if m[ns[1]][ns[0]] != '#':
                    yield ns
        else:
            ns = (s[0]+dirs[i][0], s[1]+dirs[i][1])
            if m[ns[1]][ns[0]] != '#':
                yield ns

target = (len(m[0])-2, len(m)-1)
maxgeneration = 0
generation = 0
prev_states, next_states = set(), {((1, 0), None, frozenset())}
while len(next_states):
    generation += 1
    prev_states, next_states = next_states, set()
    for s, last, history in prev_states:
        nls = list(neighbors(s))
        if len(nls) > 2:
            # not enitrely correct if there are multiple inputs to >^<V
            # but this isn't the case for the input data
            history |= {s}
        for ns in neighbors(s):
            if ns != last and ns not in history:
                if ns == target:
                    maxgeneration = generation
                else:
                    next_states.add((ns, s, history))
print(maxgeneration)
