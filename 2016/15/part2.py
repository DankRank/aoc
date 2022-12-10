#!/usr/bin/env python3
discs = []
try:
    while True:
        line = input().split()
        m = int(line[3])
        a = int(line[11][:-1]) + int(line[1][1:])
        discs.append([m, a])
except EOFError:
    pass
discs.append([11, len(discs)+1])
discs.sort(reverse=True)
step = 0
incr = 1
disc = 0
while disc < len(discs):
    if (discs[disc][1]+step) % discs[disc][0] != 0:
        step += incr
    else:
        incr *= discs[disc][0]
        disc += 1
print(step)
