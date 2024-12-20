#!/usr/bin/env python3
s = input()

alphabet = [ch for ch in range(26) if chr(ch+97) not in 'iol']

class Found(Exception):
    def __init__(self, s):
        self.s = s

def nextpwd(s):
    s = [ord(ch)-97 for ch in s]
    ns = list(s)
    def dfs(i, bigger, haspair1, haspair2, hasstraight):
        if i == len(s):
            if bigger and haspair1 and haspair2 and hasstraight:
                raise Found(''.join(chr(ch+97) for ch in ns))
            return
        if i == len(s)-2 and not haspair1:
            return
        for ch in alphabet:
            if bigger or ch >= s[i]:
                nbigger = bigger or ch > s[i]
                nhaspair1 = haspair1 or (i>0 and ch == ns[i-1])
                nhaspair2 = haspair2 or (i>2 and haspair1 and ch == ns[i-1] and (ch != ns[i-2] or ch == ns[i-3]))
                nhasstraight = hasstraight or (i>1 and ch == ns[i-1]+1 and ch == ns[i-2]+2)
                ns[i] = ch
                dfs(i+1, nbigger, nhaspair1, nhaspair2, nhasstraight)
    try:
        dfs(0, False, False, False, False)
    except Found as e:
        return e.s

s = nextpwd(s)
print(s)
s = nextpwd(s)
print(s)
