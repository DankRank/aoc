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

triplets = {}
for a, b in m:
    for c in adj[a]&adj[b]:
        triplets[frozenset((a, b, c))] = adj[a]&adj[b]&adj[c]

next_tuplets = triplets
while len(next_tuplets):
    prev_tuplets, next_tuplets = next_tuplets, {}
    for k, v in prev_tuplets.items():
        for c in v:
            next_tuplets[k.union((c,))] = v&adj[c]

assert len(prev_tuplets) == 1
for tuplet in prev_tuplets:
    print(','.join(sorted(tuplet)))
