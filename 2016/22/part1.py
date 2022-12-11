#!/usr/bin/env python3
import bisect
input()
input()
nodes = []
try:
    while True:
        nodes.append(tuple(int(s.rstrip('T')) for s in input().split()[2:4]))
except EOFError:
    pass
av = sorted(map(lambda x: x[1], nodes))

count = 0
for node in nodes:
    if node[0] != 0:
        count += len(av)-bisect.bisect_left(av, node[0])
        if node[1] >= node[0]:
            count -= 1
print(count)
