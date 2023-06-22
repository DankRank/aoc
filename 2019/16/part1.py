#!/usr/bin/env python3
wave = [int(x) for x in input()]
n = len(wave)
mat = [[[0, 1, 0, -1][(k+1)//(j+1)%4] for k in range(n)] for j in range(n)]
for i in range(100):
    wave = [abs(sum(mat[j][k]*wave[k] for k in range(n)))%10 for j in range(n)]
print(''.join(str(x) for x in wave[:8]))
