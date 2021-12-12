#!/usr/bin/env python3
graph = {}
try:
    while True:
        a, b = input().split('-')
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
except EOFError:
    pass

count = 0
visited = set()
def rec(node):
    global count
    if node[0].islower():
        visited.add(node)
    for dst in graph[node]:
        if dst == 'end':
            count += 1
        elif dst not in visited:
            rec(dst)
    visited.discard(node)
rec('start')
print(count)
