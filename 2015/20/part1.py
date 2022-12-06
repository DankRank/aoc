#!/usr/bin/env python3
import math
num = int(input())//10
# Divide A034885 by A002093 to see why dividing by 3 is pretty safe
div = 3
pregen = 7
pregenf = math.factorial(pregen)
arr = [0]*pregenf
for i in range(1, pregen+1):
    for j in range(i, pregenf, i):
        arr[j%pregenf] += i

arr = arr*math.ceil((num//div/pregenf))
for i in range(pregen+1, num//div):
    for j in range(i, num//div, i):
        arr[j] += i
    if arr[i] >= num:
        print(i)
        break
