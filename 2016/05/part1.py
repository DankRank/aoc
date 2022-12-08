#!/usr/bin/env python3
import hashlib
key = input().encode()
index = 0
pwd = ''
while len(pwd) < 8:
    h = hashlib.md5()
    h.update(key)
    h.update(str(index).encode())
    d = h.hexdigest()
    if d[:5] == '00000':
        pwd += d[5]
    index += 1
print(pwd)
