#!/usr/bin/env python3
ocmap = { '(': ')', '[': ']', '{': '}', '<': '>' }
scoremap = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
score = 0
try:
    while True:
        s = input()
        stack = []
        for c in s:
            if c in ocmap:
                stack.append(ocmap[c])
            elif c != stack.pop():
                score += scoremap[c]
                break
except EOFError:
    pass
print(score)
