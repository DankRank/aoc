assert comp[r0][r0] == r0
assert comp[r0][r1] == r1
assert comp[r0][r2] == r2
assert comp[r0][r3] == r3
assert comp[r0][m1] == m1
assert comp[r0][m2] == m2
assert comp[r0][d1] == d1
assert comp[r0][d2] == d2

assert comp[r1][r0] == r1
assert comp[r1][r1] == r2
assert comp[r1][r2] == r3
assert comp[r1][r3] == r0
assert comp[r1][m1] == d2
assert comp[r1][m2] == d1
assert comp[r1][d1] == m1
assert comp[r1][d2] == m2

assert comp[r2][r0] == r2
assert comp[r2][r1] == r3
assert comp[r2][r2] == r0
assert comp[r2][r3] == r1
assert comp[r2][m1] == m2
assert comp[r2][m2] == m1
assert comp[r2][d1] == d2
assert comp[r2][d2] == d1

assert comp[r3][r0] == r3
assert comp[r3][r1] == r0
assert comp[r3][r2] == r1
assert comp[r3][r3] == r2
assert comp[r3][m1] == d1
assert comp[r3][m2] == d2
assert comp[r3][d1] == m2
assert comp[r3][d2] == m1

assert comp[m1][r0] == m1
assert comp[m1][r1] == d1
assert comp[m1][r2] == m2
assert comp[m1][r3] == d2
assert comp[m1][m1] == r0
assert comp[m1][m2] == r2
assert comp[m1][d1] == r1
assert comp[m1][d2] == r3

assert comp[m2][r0] == m2
assert comp[m2][r1] == d2
assert comp[m2][r2] == m1
assert comp[m2][r3] == d1
assert comp[m2][m1] == r2
assert comp[m2][m2] == r0
assert comp[m2][d1] == r3
assert comp[m2][d2] == r1

assert comp[d1][r0] == d1
assert comp[d1][r1] == m2
assert comp[d1][r2] == d2
assert comp[d1][r3] == m1
assert comp[d1][m1] == r3
assert comp[d1][m2] == r1
assert comp[d1][d1] == r0
assert comp[d1][d2] == r2

assert comp[d2][r0] == d2
assert comp[d2][r1] == m1
assert comp[d2][r2] == d1
assert comp[d2][r3] == m2
assert comp[d2][m1] == r1
assert comp[d2][m2] == r3
assert comp[d2][d1] == r2
assert comp[d2][d2] == r0
