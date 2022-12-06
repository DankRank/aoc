#!/usr/bin/env python3
line = input()
for i in range(len(line)-3):
    if len(set(line[i:i+4])) == 4:
        break
print(i+4)
