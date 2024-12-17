#!/usr/bin/env python3
regs = [int(input().split(': ')[1]) for i in range(3)]
input()
program = [int(x) for x in input().split(': ')[1].split(',')]

def getdigit(a):
    return (a ^ 1 ^ (a >> ((a&7)^2)))&7

class Found(Exception):
    def __init__(self, a):
        self.a = a

def dfs(i, a):
    if i == -1:
        raise Found(a)
    a <<= 3
    for n in range(8):
        if program[i] == getdigit(a|n):
            dfs(i-1, a|n)

try:
    dfs(len(program)-1, 0)
except Found as e:
    print(e.a)
