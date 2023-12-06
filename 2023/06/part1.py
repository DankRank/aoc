#!/usr/bin/env python3
times = [int(x) for x in input().split()[1:]]
dists = [int(x) for x in input().split()[1:]]
s = 1
for t, d in zip(times, dists):
    wins = 0
    for i in range(1, t):
        if (t-i)*i > d:
            wins += 1
    s *= wins
print(s)
