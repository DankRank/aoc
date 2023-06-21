#!/usr/bin/env python3
import sys
srctext = [int(line) for line in input().split(',')]
for noun in range(100):
    for verb in range(100):
        text = srctext.copy()
        text[1] = noun
        text[2] = verb
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
        if text[0] == 19690720:
            print(100*noun + verb)
            sys.exit(0)
