#!/usr/bin/env python3
rates = {}
tunnels = {}
try:
    while True:
        line = input().split()
        valve = line[1]
        if line[4][5:-1] != '0':
            rates[valve] = int(line[4][5:-1])
        tunnels[valve] = set(s.rstrip(',') for s in line[9:])
except EOFError:
    pass
dists = {}

def bfs(init):
    known_states = {init}
    prev_states = set()
    next_states = {init}
    generation = 0
    while len(next_states) > 0:
        prev_states, next_states = next_states, set()
        generation += 1
        for s in prev_states:
            for ns in tunnels[s]:
                if ns not in known_states:
                    if ns in rates:
                        dists[(init, ns)] = generation
                    known_states.add(ns)
                    next_states.add(ns)
bfs('AA')
for s in rates:
    bfs(s)

nodes = list(rates)
nodes.sort(key=lambda x: rates[x])
s = 'AA'
visited = ['AA']
value = 0
time = 0
stack = []
i = 0
maxvalue = 0
maxvisited = []
while len(stack) > 0 or i < len(nodes):
    ns = nodes[i]
    if ns not in visited:
        if time + dists[(s, ns)] + 1 <= 26:
            stack.append((s, i+1, value, time))
            visited.append(ns)
            time += dists[(s, ns)] + 1
            value += rates[ns]*(26-time)
            if value > maxvalue:
                maxvalue = value
                maxvisited = list(visited)
            s = ns
            i = 0
        else:
            i += 1
    else:
        i += 1
    while i == len(nodes):
        if len(stack) == 0:
            break
        s, i, value, time = stack.pop()
        visited.pop()
# elephant's turn
s = 'AA'
visited = maxvisited
value = maxvalue
time = 0
i = 0
while len(stack) > 0 or i < len(nodes):
    ns = nodes[i]
    if ns not in visited:
        if time + dists[(s, ns)] + 1 <= 26:
            stack.append((s, i+1, value, time))
            visited.append(ns)
            time += dists[(s, ns)] + 1
            value += rates[ns]*(26-time)
            if value > maxvalue:
                maxvalue = value
            s = ns
            i = 0
        else:
            i += 1
    else:
        i += 1
    while i == len(nodes):
        if len(stack) == 0:
            break
        s, i, value, time = stack.pop()
        visited.pop()
print(maxvalue)
