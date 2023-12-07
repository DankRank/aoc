#!/usr/bin/env python3
def cardstrength(s):
    if s == 'A':
        return 14
    if s == 'K':
        return 13
    if s == 'Q':
        return 12
    if s == 'J':
        return 1
    if s == 'T':
        return 10
    return int(s)

def handstrength(s):
    origcards = [cardstrength(x) for x in s]
    gs = []
    count, last = 0, -1
    last = -1
    for i in sorted(origcards, reverse=True):
        if i != last:
            if last != -1:
                gs.append((count, last))
            count, last = 0, i
        count += 1
    joker = last == 1 and count != 5
    if not joker:
        gs.append((count, last))
    gs.sort(key=lambda x: -x[0])
    if joker:
        gs[0] = (gs[0][0] + count, gs[0][1])
    counts, cards = zip(*gs)
    cards = origcards # I don't think this is how poker works
    if counts[0] == 5:
        return (7, *cards) # five of a kind
    elif counts[0] == 4:
        return (6, *cards) # four of a kind
    elif counts[0] == 3:
        if counts[1] == 2:
            return (5, *cards) # full house
        else:
            return (4, *cards) # three of a kind
    elif counts[0] == 2:
        if counts[1] == 2:
            return (3, *cards) # two pair
        else:
            return (2, *cards) # one pair
    else:
        return (1, *cards) # high card

hands = []
try:
    while True:
        hand, bid = input().split()
        hands.append((hand, int(bid)))
except EOFError:
    pass

hands.sort(key=lambda x: handstrength(x[0]))
print(sum((a+1)*b[1] for a, b in enumerate(hands)))
