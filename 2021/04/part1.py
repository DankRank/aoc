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
    for roll in rolls:
        rollSet.add(roll)
        for card in cards:
            for row in chain(card, map(list, zip(*card))):
                if rollSet.issuperset(row):
                    return sum(filter(lambda x: x not in rollSet, chain(*card))) * roll
print(findBingo(rolls, cards))
