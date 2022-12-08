#!/usr/bin/env python3
row, col = map(lambda x: int(x[:-1]), input().split()[-3::2])
rc = col+row-1
print(20151125*pow(252533, rc*(rc+1)//2 - (row-1) - 1, 33554393)%33554393)
