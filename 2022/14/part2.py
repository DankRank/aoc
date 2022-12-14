#!/usr/bin/env python3
sand_source = (500, 0)
paths = []
try:
    while True:
        path = list(tuple(int(c) for c in line.split(',')) for line in input().split(' -> '))
        paths.append(path)
except EOFError:
    pass
minx = min(n[0] for path in paths for n in path)
miny = min(n[1] for path in paths for n in path)
maxx = max(n[0] for path in paths for n in path)
maxy = max(n[1] for path in paths for n in path)
assert minx >= 0 and maxx >= 0 and miny >= 0 and maxy >= 0
maxy += 2
assert maxy < 500
maxx += maxy
mapp = [['.']*(maxx+2) for i in range (maxy+1)]
for path in paths:
    for a, b in zip(path, path[1:]):
        if a[0] == b[0]:
            for i in range(min(a[1], b[1]), max(a[1], b[1])+1):
                mapp[i][a[0]] = '#'
        else:
            assert a[1] == b[1]
            for i in range(min(a[0], b[0]), max(a[0], b[0])+1):
                mapp[a[1]][i] = '#'
for i in range(maxx):
    mapp[maxy][i] = '#'

count = 0
sand = sand_source
while mapp[sand_source[1]][sand_source[0]] == '.':
    if mapp[sand[1]+1][sand[0]] == '.':
        sand = (sand[0], sand[1]+1)
    elif mapp[sand[1]+1][sand[0]-1] == '.':
        sand = (sand[0]-1, sand[1]+1)
    elif mapp[sand[1]+1][sand[0]+1] == '.':
        sand = (sand[0]+1, sand[1]+1)
    else:
        mapp[sand[1]][sand[0]] = 'O'
        count += 1
        sand = sand_source
print(count)
