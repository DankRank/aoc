#!/usr/bin/env python3
import math
num = int(input())
# I have no proof, but this works lol
div = 3*11
arr = [0]*(num//div)
for i in range(1, num//div):
    for j in range(i, min(num//div, i*51), i):
        arr[j] += i*11
    if arr[i] >= num:
        print(i)
        break
