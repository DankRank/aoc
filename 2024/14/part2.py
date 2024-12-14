#!/usr/bin/env python3
import sys
import time
m = [[[int(x) for x in pair.split('=')[1].split(',')] for pair in line.rstrip().split()] for line in sys.stdin]
w, h = 101, 103

view = [[0]*w for i in range(h)]
for p, v in m:
    view[p[1]][p[0]] += 1
def advanceby(step):
    for p, v in m:
        view[p[1]][p[0]] -= 1
        p[0] = (p[0] + v[0]*step) % w
        p[1] = (p[1] + v[1]*step) % h
        view[p[1]][p[0]] += 1
def show(label):
    print('\x1B[2J', end='')
    print(label)
    print(*(''.join('#' if x else ' ' for x in line) for line in view), sep='\n')

#advanceby(4)
#advanceby(29)
#step = 1
#for i in range(0, w*h, step):
#    time.sleep(0.300)
#    show(i)
#    advanceby(step)

# anomalies at 29+k*w and 4+k*h
a = 29 # vertical anomaly
b = 4 # horizontal anomaly
q = 0
def crt(a1, m1, a2, m2):
    n1 = pow(m1, -1, m2)
    n2 = pow(m2, -1, m1)
    m = m1*m2
    return (a1*n2*m2 + a2*n1*m1)%m, m
print(crt(a, w, b, h)[0])
