#!/usr/bin/env python3
import sys
import math
aset = {(x,y) for y, line in enumerate(sys.stdin) for x, c in enumerate(line.rstrip()) if c == '#'}
alist = list(aset)
count = {k:0 for k in alist}
for idx, a in enumerate(alist):
    for b in alist[idx+1:]:
        x, y = a
        dx = b[0] - x
        dy = b[1] - y
        d = math.gcd(dx, dy)
        dx //= d
        dy //= d
        for i in range(1,d):
            x += dx
            y += dy
            if (x, y) in aset:
                break
        else:
            count[a] += 1
            count[b] += 1
base, maxcount = max(count.items(), key=lambda x: x[1])
print(maxcount)

buckets = {}
for b in alist:
    if base != b:
        dx = b[0] - base[0]
        dy = b[1] - base[1]
        d = math.gcd(dx, dy)
        bucket = dx//d, dy//d
        if bucket not in buckets:
            buckets[bucket] = [math.atan2(dx//d, -dy//d)]
        buckets[bucket].append((dx,dy))
buckets = sorted(buckets.values(), key=lambda x: x[0]+2*math.pi if x[0] < 0 else x[0])
for bucket in buckets:
    bucket.pop(0)
    bucket.sort(key=lambda x: (abs(x[0]), abs(x[1])))
i = 0
for n in range(200):
    while len(buckets[i]) == 0:
        i += 1
        if i == len(buckets):
            i = 0
    v = buckets[i].pop()
    i += 1
    if i == len(buckets):
        i = 0
print((base[0]+v[0])*100 + base[1]+v[1])
