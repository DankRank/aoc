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
visitedTwice = False
def rec(node):
    global count, visitedTwice
    shouldDiscard = node not in visited
    if node[0].islower():
        visited.add(node)
    for dst in graph[node]:
        if dst == 'end':
            count += 1
        elif dst not in visited:
            rec(dst)
        elif not visitedTwice and dst != 'start':
            visitedTwice = True
            rec(dst)
            visitedTwice = False
    if shouldDiscard:
        visited.discard(node)
rec('start')
print(count)
