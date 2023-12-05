#!/usr/bin/env python3
from bisect import bisect_right
seeds = [int(x) for x in input().split(': ')[1].split()]
seeds = {range(a, a+b): 0 for a,b in zip(seeds[::2], seeds[1::2])}
input()
input()
maps = [{}]
try:
    while True:
        line = input()
        if line == '':
            maps.append({})
            input()
            continue
        dst, src, size = (int(x) for x in line.split())
        maps[-1][range(src,src+size)] = dst-src
except EOFError:
    pass
def remap(ma, mb):
    st = list(ma.items())
    ls = sorted(mb.items(), key=lambda x: x[0].start)
    while len(st):
        s, t = st.pop()
        i = bisect_right(ls, s.start+t, key=lambda x: x[0].start)
        if i:
            k, v = ls[i-1]
            if s.start+t < k.stop and k.start < s.stop+t:
                start = max(s.start+t, k.start)-t
                stop = min(s.stop+t, k.stop)-t
                yield range(start, stop), t+v
                if s.start < start:
                    st.append((range(s.start, start), t))
                if stop < s.stop:
                    st.append((range(stop, s.stop), t))
            else:
                yield s, t
        else:
            yield s, t
for m in maps:
    seeds = dict(remap(seeds, m))
print(min(k.start+v for k, v in seeds.items()))
