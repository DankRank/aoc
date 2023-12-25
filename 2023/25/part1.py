#!/usr/bin/env python3
m = {}
nodes = set()
graph = 'graph {'
try:
    while True:
        k, v = input().split(': ')
        nodes.add(k)
        if k not in m:
            m[k] = set()
        for v in v.split():
            nodes.add(v)
            if v not in m:
                m[v] = set()
            m[k].add(v)
            m[v].add(k)
            graph += f'\n\t{k} -- {v}'
except EOFError:
    pass
graph += '\n}\n'
#print(graph)

# FIXME: input dependent
m['bvc'].remove('rsm')
m['rsm'].remove('bvc')
m['zmq'].remove('pgh')
m['pgh'].remove('zmq')
m['bkm'].remove('ldk')
m['ldk'].remove('bkm')

cluster = {}
clumembers = {}

while len(nodes):
    n = nodes.pop()
    if n not in cluster:
        cluster[n] = n
        clumembers[n] = {n}
    newclu = cluster[n]
    for i in m[n]:
        if i in cluster:
            oldclu = cluster[i]
            if newclu != oldclu:
                clumembers[newclu] |= clumembers[oldclu]
                for j in clumembers[oldclu]:
                    cluster[j] = newclu
                del clumembers[oldclu]
        else:
            clumembers[newclu].add(i)
            cluster[i] = newclu

a, b = (len(x) for x in clumembers.values())
print(a*b)
