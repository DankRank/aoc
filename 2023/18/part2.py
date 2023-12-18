#!/usr/bin/env python3
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dmap = {'0':0, '1':3, '2':2, '3':1}
shape = []
n = 0
try:
    while True:
        s = input().split()[2][2:-1]
        d, r = dmap[s[-1]], int(s[:-1], 16)
        shape.append([d, r])
except EOFError:
    pass

# compute normals (which point inside the shape)
shape[0].append((shape[0][0]-1)&3) # FIXME: this is just a guess. if it's wrong, change to +1
for i in range(1, len(shape)):
    if shape[i][0] == shape[i-1][2]: # convex turn
        shape[i].append(shape[i-1][0]^2)
    else: # concave turn
        shape[i].append(shape[i-1][0])

count = 0
def checksegment(i):
    global count
    if shape[i][1] == 0:
        del shape[i]
        if i and i < len(shape) and shape[i-1][0]&1 == shape[i][0]&1:
            if shape[i-1][0] == shape[i][0]:
                assert shape[i-1][2] == shape[i][2]
                shape[i-1][1] += shape[i][1]
            else:
                assert shape[i-1][2] == shape[i][2]^2
                count += shape[i][1]
                shape[i-1][1] -= shape[i][1]
            del shape[i]

def optimize():
    global count
    rv = False
    i = 0
    while i < len(shape)-2:
        if shape[i][0] == shape[i+2][0]^2:
            m = min(shape[i][1], shape[i+2][1])
            if shape[i][2] == shape[i+1][0]:
                count += m*(shape[i+1][1]+1)
            else:
                count -= m*(shape[i+1][1]-1)
            shape[i][1] -= m
            shape[i+2][1] -= m
            checksegment(i+2)
            checksegment(i)
            rv = True
        else:
            i += 1
    return rv
while optimize():
    pass
assert len(shape) == 1 and shape[0][1] == 0
print(count+1)
