#!/usr/bin/env python3
count = 0
def check(line):
    for i in range(len(line)//2):
        k = line[i*2]
        v = int(line[i*2+1])
        if k == 'children:':
            if v != 3: return False
        elif k == 'cats:':
            if v <= 7: return False
        elif k == 'samoyeds:':
            if v != 2: return False
        elif k == 'pomeranians:':
            if v >= 3: return False
        elif k == 'akitas:':
            if v != 0: return False
        elif k == 'vizslas:':
            if v != 0: return False
        elif k == 'goldfish:':
            if v >= 5: return False
        elif k == 'trees:':
            if v <= 3: return False
        elif k == 'cars:':
            if v != 2: return False
        elif k == 'perfumes:':
            if v != 1: return False
    return True
try:
    while True:
        line = input().replace(',', '').split()[2:]
        count += 1
        if check(line):
            print(count)
except EOFError:
    pass
