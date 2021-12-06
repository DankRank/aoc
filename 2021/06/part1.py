#!/usr/bin/env python3
fish = list(map(int, input().split(',')))
def simStep(fish):
    newCount = sum(1 for x in filter(lambda x: x == 0, fish))
    return list(map(lambda x: 6 if x==0 else x-1, fish)) + [8]*newCount
for i in range(80):
    fish = simStep(fish)
print(len(fish))
