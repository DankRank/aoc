#!/usr/bin/env python3
import sys
import itertools
ITEMS = 8
mapp = sys.stdin.read().splitlines()
locs = [None]*ITEMS
for r, line in enumerate(mapp):
    for c, ch in enumerate(line):
        if ch != '.' and ch != '#':
            locs[int(ch)] = (r, c)
assert all(loc is not None for loc in locs)
def neighbors(s):
    yield (s[0]+1, s[1])
    yield (s[0]-1, s[1])
    yield (s[0], s[1]+1)
    yield (s[0], s[1]-1)
def bfs(i):
    paths = [None]*ITEMS
    paths[i] = 0
    count = 1
    known_states = {locs[i]}
    next_states = {locs[i]}
    prev_states = set()
    generation = 0
    while count < ITEMS:
        prev_states, next_states = next_states, set()
        generation += 1
        assert len(prev_states) > 0
        for s in prev_states:
            for ns in neighbors(s):
                c = mapp[ns[0]][ns[1]]
                if c != '#' and ns not in known_states:
                    known_states.add(ns)
                    next_states.add(ns)
                    if c != '.':
                        paths[int(c)] = generation
                        count += 1
    assert all(path is not None for path in paths)
    return paths
paths = [bfs(i) for i in range(ITEMS)]

shortest_path1 = float('inf')
shortest_path2 = float('inf')
for p in itertools.permutations(range(1,ITEMS)):
    shortest_path1 = min(shortest_path1, paths[0][p[0]] + sum(paths[a][b] for a, b in zip(p,p[1:])))
    shortest_path2 = min(shortest_path2, paths[0][p[0]] + sum(paths[a][b] for a, b in zip(p,p[1:])) + paths[p[-1]][0])
print(shortest_path1)
print(shortest_path2)
