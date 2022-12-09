#!/usr/bin/env python3
# To reduce the number of states, we throw away the names of the generator-chip
# pairs, and sort them by the floor numbers.
initial_state = (1, (1,1), (1,2), (1,2), (3,3), (3,3))
target_state = (4, (4,4), (4,4), (4,4), (4,4), (4,4))
def check(s):
    s = s[1:]
    return len(set(x[1] for x in filter(lambda x: x[0]!=x[1], s)) & set(x[0] for x in s)) == 0
def derive_state(s, level, item, part):
    tup = (level, s[item][1]) if part == 0 else (s[item][0], level)
    return (level,)+tuple(sorted(s[1:item]+(tup,)+s[item+1:]))
def derive_state2(s, level, item1, part1, item2, part2):
    if item1 == item2:
        return (level,)+tuple(sorted(s[1:item1]+((level, level),)+s[item1+1:]))
    else:
        if item1 > item2:
            item1, part1, item2, part2 = item2, part2, item1, part1
        tup1 = (level, s[item1][1]) if part1 == 0 else (s[item1][0], level)
        tup2 = (level, s[item2][1]) if part2 == 0 else (s[item2][0], level)
        return (level,)+tuple(sorted(s[1:item1]+(tup1,)+s[item1+1:item2]+(tup2,)+s[item2+1:]))
def gen_repls(s):
    for i in range(1, len(s)):
        if s[i][0] == s[0]:
            yield i, 0
        if s[i][1] == s[0]:
            yield i, 1
def gen_states(s):
    repls = list(gen_repls(s))
    if s[0] > 1:
        for i in range(len(repls)):
            yield derive_state(s, s[0]-1, *repls[i])
            for j in range(i+1, len(repls)):
                yield derive_state2(s, s[0]-1, *repls[i], *repls[j])
    if s[0] < 4:
        for i in range(len(repls)):
            yield derive_state(s, s[0]+1, *repls[i])
            for j in range(i+1, len(repls)):
                yield derive_state2(s, s[0]+1, *repls[i], *repls[j])
def solve(init, fini):
    known_states = {init}
    next_states = {init}
    last_states = set()
    generation = 0
    while fini not in known_states:
        generation += 1
        last_states, next_states = next_states, set()
        assert len(last_states) > 0
        for s in last_states:
            ls = [s for s in gen_states(s) if s not in known_states and check(s)]
            known_states.update(ls)
            next_states.update(ls)
    return generation
print(solve(initial_state, target_state))
initial_state = (initial_state[0],) + ((1,1), (1,1)) + initial_state[1:]
target_state += ((4,4), (4,4))
print(solve(initial_state, target_state))
