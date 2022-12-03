#!/usr/bin/env python3
class Deer:
    def __init__(self, vel, gotime, resttime):
        self.vel = vel
        self.gotime = gotime
        self.resttime = resttime
        self.dist = 0
        self.score = 0
    def step(self, t):
        if t%(self.gotime+self.resttime) < self.gotime:
            self.dist += self.vel
deer = []
try:
    while True:
        line = input().split()
        deer.append(Deer(int(line[3]), int(line[6]), int(line[13])))
except EOFError:
    pass
for t in range(2503):
    for d in deer:
        d.step(t)
    maxd = max(d.dist for d in deer)
    for d in deer:
        if d.dist == maxd:
            d.score += 1
print(max(d.score for d in deer))
