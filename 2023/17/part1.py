#!/usr/bin/env python3
import sys
import queue
m = [[int(x) for x in line.rstrip()] for line in sys.stdin]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
assert len(m) == len(m[0])
target = (len(m[0])-1, len(m)-1)
minp = sum(m[i][i] + m[i-1][i] for i in range(1, len(m)))
# node format: x, y, last direction, repeat count
def neighbors(s):
    for i, d, in enumerate(dirs):
        if s[2]^2 != i and (s[2] != i or s[3] < 3):
            if s[0]+d[0] in range(len(m[0])) and s[1]+d[1] in range(len(m)):
                if s[2] != i:
                    yield s[0]+d[0], s[1]+d[1], i, 1
                else:
                    yield s[0]+d[0], s[1]+d[1], s[2], s[3]+1
dist = {(0, 0, 0, 0): 0}
visited = set()
q = queue.PriorityQueue()
q.put((0, (0, 0, 0, 0)))
while not q.empty():
    s = q.get()[1]
    if s in visited:
        continue
    for ns in neighbors(s):
        if ns not in visited:
            ndist = dist[s]+m[ns[1]][ns[0]]
            if ns not in dist or ndist < dist[ns]:
                dist[ns] = ndist
                if ns[:2] == target and ndist < minp:
                    minp = ndist
                elif ndist < minp:
                    q.put((ndist, ns))
    visited.add(s)
print(minp)
