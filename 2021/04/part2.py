#!/usr/bin/env python3
from itertools import chain
rolls = list(map(int, input().split(',')))
cards = []
try:
    while True:
        input()
        card = []
        for i in range(5):
            card.append(list(map(int, input().split())))
        cards.append(card)
except EOFError:
    pass
def findBingo(rolls, cards):
    rollSet = set()
    lastWin = -1
    for roll in rolls:
        rollSet.add(roll)
        pendingRemove = []
        for card in cards:
            for row in chain(card, map(list, zip(*card))):
                if rollSet.issuperset(row):
                    lastWin = sum(filter(lambda x: x not in rollSet, chain(*card))) * roll
                    pendingRemove.append(card)
                    break
        cards = list(filter(lambda x: x not in pendingRemove, cards))
    return lastWin
print(findBingo(rolls, cards))
