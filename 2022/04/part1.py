#!/usr/bin/env python3
import re
count1 = 0
count2 = 0
try:
    while True:
        a,b,c,d = map(int, re.split('[-,]', input()))
        if (c >= a and d <= b) or (a >= c and b <= d):
            count1 += 1
        if (b >= c and a <= d):
            count2 += 1
except EOFError:
    pass
print(count1)
print(count2)
