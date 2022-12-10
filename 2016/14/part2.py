#!/usr/bin/env python3
import hashlib
import functools
salt = input().encode()
@functools.lru_cache(1100)
def gethash(i):
    h = hashlib.md5()
    h.update(salt)
    h.update(str(i).encode())
    for i in range(2016):
        d = h.hexdigest().encode()
        h = hashlib.md5()
        h.update(d)
    return h.hexdigest()
index = 0
keys = []
while len(keys) < 64:
    d = gethash(index)
    for i in range(32-2):
        if d[i] == d[i+1] and d[i+1] == d[i+2]:
            s = d[i]*5
            if any(s in gethash(i) for i in range(index+1, index+1001)):
                keys.append(index)
            break
    index += 1
print(keys[63])
