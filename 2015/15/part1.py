#!/usr/bin/env python3
ings = []
try:
    while True:
        line = input().split()
        ings.append([int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])])
except EOFError:
    pass
assert len(ings) == 4
res1 = 0
res2 = 0
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            a = ings[0][0]*i + ings[1][0]*j + ings[2][0]*k + ings[3][0]*(100-i-j-k)
            b = ings[0][1]*i + ings[1][1]*j + ings[2][1]*k + ings[3][1]*(100-i-j-k)
            c = ings[0][2]*i + ings[1][2]*j + ings[2][2]*k + ings[3][2]*(100-i-j-k)
            d = ings[0][3]*i + ings[1][3]*j + ings[2][3]*k + ings[3][3]*(100-i-j-k)
            if a > 0 and b > 0 and c > 0 and d > 0:
                res1 = max(res1, a*b*c*d)
                e = ings[0][4]*i + ings[1][4]*j + ings[2][4]*k + ings[3][4]*(100-i-j-k)
                if e == 500:
                    res2 = max(res2, a*b*c*d)
print(res1)
print(res2)
