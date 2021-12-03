#!/usr/bin/env python3
counts = [0 for i in range(12)]
try:
    while True:
        s = input()
        for i in range(len(s)):
            counts[i] += 1 if s[i] == '1' else -1
except EOFError:
    pass
gamma = int(''.join(['1' if x>0 else '0' for x in counts]), 2)
epsilon = gamma ^ 0xfff
print(gamma * epsilon)
