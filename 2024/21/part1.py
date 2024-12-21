#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
kp1coords = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
}
kp1exclude = (0, 3)
kp2coords = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}
kp2exclude = (0, 0)

def move(src, dst, exclude):
    dx = dst[0]-src[0]
    dy = dst[1]-src[1]
    cx = '>' if dx > 0 else '<'
    cy = 'v' if dy > 0 else '^'
    mov1 = cx*abs(dx)
    mov2 = cy*abs(dy)
    if dx and dy:
        if src[0] == exclude[0] and dst[1] == exclude[1]:
            return mov1 + mov2 + 'A',
        elif src[1] == exclude[1] and dst[0] == exclude[0]:
            return mov2 + mov1 + 'A',
        else:
            return mov1 + mov2 + 'A', mov2 + mov1 + 'A'
    else:
        return mov1 + mov2 + 'A',

def typein(s, coords, movefunc):
    pos = coords['A']
    ns = ''
    for ch in s:
        dst = coords[ch]
        ns += movefunc(pos, dst)
        pos = dst
    return ns

def movebot3(src, dst):
    paths = move(src, dst, kp2exclude)
    return min(paths, key=len)
def movebot2(src, dst):
    paths = move(src, dst, kp2exclude)
    paths = [typein(path, kp2coords, movebot3) for path in paths]
    return min(paths, key=len)
def movebot1(src, dst):
    paths = move(src, dst, kp1exclude)
    paths = [typein(path, kp2coords, movebot2) for path in paths]
    return min(paths, key=len)

count = 0
for s in m:
    ns = typein(s, kp1coords, movebot1)
    count += len(ns) * int(s[:-1])
print(count)
