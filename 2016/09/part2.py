#!/usr/bin/env python3
def find_dlen(s):
    p = 0
    count = 0
    while p < len(s):
        lp = s.find('(', p)
        if lp == -1:
            count += len(s)-p
            break
        count += lp - p
        rp = s.find(')', lp)
        a, b = map(int, s[lp+1:rp].split('x'))
        count += b*find_dlen(s[rp+1:rp+1+a])
        p = rp+1+a
    return count
print(find_dlen(input()))
