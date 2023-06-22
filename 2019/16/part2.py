#!/usr/bin/env python3
wave = [int(x) for x in input()]*10000
n = len(wave)
ofs = int(''.join(str(x) for x in wave[:7]))
assert n//2 < ofs
# take advantage of the fact that lower half of the matrix looks like this
# 0 0 1 1 1
# 0 0 0 1 1
# 0 0 0 0 1
# we can precompute 100 applications of the matrix 
#x = [1,0,0,0,0,0,0,0,0,0]
#for i in range(101):
#    print(i, x)
#    for j in range(1, 10):
#        x[j] += x[j-1]
# this produces A017763, n+99 choose 99
coeff = [1]
fact = 1
for i in range(1, n-ofs):
    fact *= i+99
    fact //= i
    coeff.append(fact%10)
for i in range(ofs, ofs+8):
    wave[i] = sum(a*b for a,b in zip(wave[i:], coeff))%10
print(''.join(str(x) for x in wave[ofs:ofs+8]))
