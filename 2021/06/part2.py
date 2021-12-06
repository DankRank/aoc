#!/usr/bin/env python3
fish = [0,0,0,0,0,0,0,0,0]
for i in list(map(int, input().split(','))):
    fish[i] += 1
def simStep(fish):
    fish = fish[1:] + fish[0:1]
    fish[6] += fish[8]
    return fish
for i in range(256):
    fish = simStep(fish)
print(sum(fish))
