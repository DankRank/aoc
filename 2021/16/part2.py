#!/usr/bin/env python3
from itertools import chain
from functools import reduce
from operator import mul
hex2bin = {
    '0': [0,0,0,0], '1': [0,0,0,1], '2': [0,0,1,0], '3': [0,0,1,1],
    '4': [0,1,0,0], '5': [0,1,0,1], '6': [0,1,1,0], '7': [0,1,1,1],
    '8': [1,0,0,0], '9': [1,0,0,1], 'A': [1,0,1,0], 'B': [1,0,1,1],
    'C': [1,1,0,0], 'D': [1,1,0,1], 'E': [1,1,1,0], 'F': [1,1,1,1],
}
bits = list(chain(*map(lambda x: hex2bin[x], input())))
bitp = 0
def read_bits(n):
    global bitp
    oldn = n
    res = 0
    while n > 0:
        res <<= 1
        res |= bits[bitp]
        bitp += 1
        n -= 1
    return res

def read_packet():
    version = read_bits(3)
    ptype = read_bits(3)

    if ptype == 4:
        more = True
        num = 0
        while more:
            more = read_bits(1) != 0
            num <<= 4
            num |= read_bits(4)
        return num
    else:
        children = []
        lentype = read_bits(1)
        if lentype == 0:
            limit = read_bits(15)
            limit += bitp
            while bitp < limit:
                children.append(read_packet())
        else:
            for i in range(read_bits(11)):
                children.append(read_packet())
        if ptype == 0:
            return sum(children)
        elif ptype == 1:
            return reduce(mul, children)
        elif ptype == 2:
            return min(children)
        elif ptype == 3:
            return max(children)
        elif ptype == 5:
            return 1 if children[0] > children[1] else 0
        elif ptype == 6:
            return 1 if children[0] < children[1] else 0
        elif ptype == 7:
            return 1 if children[0] == children[1] else 0

print(read_packet())
