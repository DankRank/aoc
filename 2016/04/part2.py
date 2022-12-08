#!/usr/bin/env python3
try:
    while True:
        line = input().rstrip(']').split('-')
        name = '-'.join(line[:-1])
        idn, cksum = line[-1].split('[')
        idn = int(idn)
        dname = ''.join(map(lambda x: ' ' if x == '-' else chr((ord(x)-ord('a')+idn)%26+ord('a')), name))
        if dname == 'northpole object storage':
            print(idn)
            break
except EOFError:
    pass
