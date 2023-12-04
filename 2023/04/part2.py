#!/usr/bin/env python3
cards = []
try:
    while True:
        win, have = input().split(': ')[1].replace('  ', ' ').lstrip().split(' | ')
        win = set(int(x) for x in win.split())
        have = set(int(x) for x in have.split())
        cards.append(len(win & have))
except EOFError:
    pass
cardcounts = [1]*len(cards)
for i in range(len(cards)-1, -1, -1):
    cardcounts[i] += sum(cardcounts[i+1:i+1+cards[i]])
print(sum(cardcounts))
