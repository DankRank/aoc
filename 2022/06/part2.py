#!/usr/bin/env python3
line = input()
for i in range(len(line)-13):
    if len(set(line[i:i+14])) == 14:
        break
print(i+14)
