#!/usr/bin/env python3
text = [int(line) for line in input().split(',')]
text[1] = 12
text[2] = 2
pc = 0
while True:
    if text[pc] == 1:
        text[text[pc+3]] = text[text[pc+1]] + text[text[pc+2]]
        pc += 4
    elif text[pc] == 2:
        text[text[pc+3]] = text[text[pc+1]] * text[text[pc+2]]
        pc += 4
    elif text[pc] == 99:
        break
    else:
        raise ValueError(f'unknown op {text[pc]} at {pc}')
print(text[0])
