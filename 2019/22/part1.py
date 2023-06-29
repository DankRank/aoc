#!/usr/bin/env python3
import sys
deck = list(range(10007))
for line in sys.stdin:
    line = line.rstrip().split()
    if line[0] == 'deal':
        if line[1] == 'into': # deal into new stack
            deck.reverse()
        else: # deal with increment
            ndeck = [None]*len(deck)
            n = int(line[3])
            for i in range(len(deck)):
                ndeck[n*i%len(deck)] = deck[i]
            deck = ndeck
    else: # cut
        n = int(line[1])
        deck = deck[n:] + deck[:n]
print(deck.index(2019))
