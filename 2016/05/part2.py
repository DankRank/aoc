#!/usr/bin/env python3
import hashlib
key = input().encode()
index = 0
pwd = [None]*8
count = 0
while count < 8:
    h = hashlib.md5()
    h.update(key)
    h.update(str(index).encode())
    d = h.hexdigest()
    if d[:5] == '00000':
        pos = int(d[5], 16)
        if pos < 8 and pwd[pos] is None:
            pwd[pos] = d[6]
            count += 1
    index += 1
print(''.join(pwd))
