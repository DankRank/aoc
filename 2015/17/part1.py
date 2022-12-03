#!/usr/bin/env python3
import sys
ls = sorted(map(int, sys.stdin.read().splitlines()), reverse=True)
res1 = 0
res2 = 0
mincount = len(ls)
count = 0
total = 0
left = sum(ls)
st = []
i = 0
while True:
    if i != len(ls) and total + ls[i] == 150:
        res1 += 1
        if count + 1 < mincount:
            mincount = count + 1
            res2 = 1
        elif count + 1 == mincount:
            res2 += 1
    if total + left >= 150 and total + ls[i] < 150:
        st.append((i, total, left, count))
        total += ls[i]
        left -= ls[i]
        count += 1
        i += 1
    elif len(st) > 0:
        if total + left < 150:
            i, total, left, count = st.pop()
        left -= ls[i]
        i += 1
    else:
        break
print(res1)
print(res2)
