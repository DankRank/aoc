#!/usr/bin/env python3
elfs = int(input())
a = [i+1 for i in range(elfs)]
i = 0
# I have no clue how this stuff works, I got it experimentally
def rhalf(p, q):
    global a, i
    half = len(a)//2
    del a[half:half+p]
    a[half:] = a[half::3]
    i = len(a)//2 + q
def lhalf(p):
    global a, i
    assert (len(a)+i+2)%3 == p
    del a[:p]
    a[:len(a)*3//4-1] = a[:len(a)*3//4-1:3]
    i = 0
rhalf(2, 1)
lhalf(1)
rhalf(1, 1)
lhalf(0)
rhalf(1, 0)
lhalf(2)
rhalf(1, 0)
lhalf(2)
rhalf(1, 1)
lhalf(1)
rhalf(2, 1)
lhalf(1)
rhalf(1, 1)
lhalf(0)
rhalf(1, 1)
lhalf(0)

while len(a) > 1:
    j = (i+len(a)//2)%len(a)
    if i < j:
        i += 1
    del a[j]
    i %= len(a)
print(a[0])
