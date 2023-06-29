#!/usr/bin/env python3
import sys
m = 119315717514047
k = 101741582076661
# calculate linear function coefficients f(x) = xa + b (mod m)
a = 1
b = 0
for line in reversed([line.rstrip().split() for line in sys.stdin]):
    if line[0] == 'deal':
        if line[1] == 'into': # deal into new stack
            a = -a
            b = m-1-b
        else: # deal with increment
            n = pow(int(line[3]), -1, m)
            a *= n
            b *= n
    else: # cut
        b += int(line[1])
a %= m
b %= m
# f^k(x) = (((xa+b)a+b)a+b)a+b...
# = xa^k + ba^k-1 + ba^k-2 + ... + ba^2 + ba + b
# = xa^k + sum(ba^i for i in range(k))
# = xa^k + b(1-a^k)/(1-a)
print((2020*pow(a, k, m) + b*(1-pow(a, k, m))*pow(1-a, -1, m))%m)
