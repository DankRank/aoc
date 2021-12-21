#!/usr/bin/env python3
p1 = int(input().split()[-1])-1
p2 = int(input().split()[-1])-1

s1 = 0
s2 = 0

dcount = 0
dstate = -1
def roll():
    global dcount, dstate
    dcount += 1
    dstate += 1
    dstate %= 100
    return dstate + 1

while True:
    p1 = (p1 + roll() + roll() + roll()) % 10
    s1 += p1 + 1
    if s1 >= 1000:
        print(s2 * dcount)
        break
    p2 = (p2 + roll() + roll() + roll()) % 10
    s2 += p2 + 1
    if s2 >= 1000:
        print(s1 * dcount)
        break
