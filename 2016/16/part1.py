#!/usr/bin/env python3
line = input()
tlen = 272
while len(line) < tlen:
    line = line + '0' + ''.join('0' if x == '1' else '1' for x in reversed(line))
line = line[:tlen]
while len(line) % 2 == 0:
    line = ''.join('0' if x != y else '1' for x, y in zip(line[::2], line[1::2]))
print(line)
