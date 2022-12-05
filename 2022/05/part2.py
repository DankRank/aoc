#!/usr/bin/env python3
H = 8
W = 9
lines = [input() for i in range(H)]
stacks = [[] for i in range(W)]
for i in range(H-1, -1, -1):
    for j in range(W):
        c = lines[i][j*4+1:j*4+2]
        if c != ' ':
            stacks[j].append(c)
input()
input()
try:
    while True:
        line = input().split()
        rep, src, dst = map(int, line[1::2])
        stacks[dst-1] += stacks[src-1][-rep:]
        del stacks[src-1][-rep:]
except EOFError:
    pass
print(''.join(stack[-1] for stack in stacks))
