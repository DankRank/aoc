#!/usr/bin/env python3
import sys
import z3
m = [sum((tuple(int(x) for x in s.split(', ')) for s in line.rstrip().split(' @ ')), start=()) for line in sys.stdin]
s = z3.Solver()
res, x, y, z, dx, dy, dz = z3.BitVecs('res x y z dx dy dz', 64)
s.add(res == x+y+z)
for i, v in enumerate(m):
    x1, y1, z1, dx1, dy1, dz1 = v
    t1 = z3.BitVec(f't{i}', 64)
    s.add(t1 > 0)
    s.add(x + dx*t1 == x1 + dx1*t1)
    s.add(y + dy*t1 == y1 + dy1*t1)
    s.add(z + dz*t1 == z1 + dz1*t1)
assert s.check() == z3.sat
m = s.model()
print(m[res])
