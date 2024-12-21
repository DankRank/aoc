#!/usr/bin/env python3
import sys
import functools
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

@functools.cache
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

def typein(s, coords, movefunc, ns=''):
    pos = coords['A']
    for ch in s:
        dst = coords[ch]
        ns += movefunc(pos, dst)
        pos = dst
    return ns

def deepcache(movefunc):
    cache = {}
    for src in kp2coords.values():
        for dst in kp2coords.values():
            cache[src, dst] = movefunc(src, dst)
    return lambda src, dst: cache[src, dst]

@deepcache
def movebot3(src, dst):
    paths = move(src, dst, kp2exclude)
    return min(paths, key=len)

def wrapmove(moveprev, stringclass=str, exclude=kp2exclude):
    def movebot(src, dst):
        paths = move(src, dst, exclude)
        paths = [typein(path, kp2coords, moveprev, stringclass()) for path in paths]
        return min(paths, key=len)
    return movebot

class NoConcatString:
    def __init__(self):
        self.strs = []
    def __iter__(self):
        def iter():
            for s in strs:
                yield from s
        return iter
    def __iadd__(self, other):
        if isinstance(other, str):
            self.strs.append(other)
        else:
            self.strs += other.strs
        return self
    def __len__(self):
        return sum(len(s) for s in self.strs)

memo_levels=17
movebot2 = movebot3
for i in range(memo_levels):
    movebot2 = deepcache(wrapmove(movebot2))
for i in range(24-memo_levels):
    movebot2 = wrapmove(movebot2, NoConcatString)

movebot1 = wrapmove(movebot2, NoConcatString, kp1exclude)

count = 0
for s in m:
    ns = typein(s, kp1coords, movebot1, NoConcatString())
    count += len(ns) * int(s[:-1])
print(count)
