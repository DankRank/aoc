#!/usr/bin/env python3

# NOTE this is broken, don't use this
for n in range(8):
    print("\tlambda x,y: ("
            +("9-" if n&1 else "  ")+("y" if n&4 else "x")+","
            +("9-" if n&2 else "  ")+("x" if n&4 else "y")+"),")

for i in range(8):
    s = ""
    for j in range(8):
        k = (j>>1&1 | j<<1&2 | j&4) if i&4 else j
        s += str(k^i)+",";
    print ("("+s+"),")


# this is for CCW and Y pointing down.
r0 = 0
m1 = 1
m2 = 2
r2 = 3
d1 = 4
r3 = 5
r1 = 6
d2 = 7
