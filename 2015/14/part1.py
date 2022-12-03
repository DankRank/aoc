#!/usr/bin/env python3
def simulate(vel, gotime, resttime, t):
    return t//(gotime+resttime) * vel*gotime + min(t%(gotime+resttime), gotime)*vel
maxd = 0
try:
    while True:
        line = input().split()
        maxd = max(maxd, simulate(int(line[3]), int(line[6]), int(line[13]), 2503))
except EOFError:
    pass
print(maxd)
