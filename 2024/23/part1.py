#!/usr/bin/env python3
import sys
m = [tuple(x for x in line.rstrip().split('-')) for line in sys.stdin]

adj = {}
for a, b in m:
    if a not in adj:
        adj[a] = {b}
    else:
        adj[a].add(b)
    if b not in adj:
        adj[b] = {a}
    else:
        adj[b].add(a)

triplets = set()
for a, b in m:
    a_or_b = a.startswith('t') or b.startswith('t')
    for c in adj[a]&adj[b]:
        if a_or_b or c.startswith('t'):
            triplets.add(frozenset((a, b, c)))
print(len(triplets))
