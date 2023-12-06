#!/usr/bin/env python3
import math
t = int(''.join(input().split()[1:]))
d = int(''.join(input().split()[1:]))
# (t-i)*i > d
# a = t/2
# b in range(t/2)
# (a-b)(a+b) > d
# a^2 - b^2 > d
# a^2 > b^2 + d
# a^2 - d > b^2
# sqrt(a^2 - d) > abs(b)
assert not t%2
x = math.sqrt((t//2)*(t//2) - d)
if x == math.floor(x):
    x -= 1
else:
    x = math.floor(x)
print(x*2 + 1)
