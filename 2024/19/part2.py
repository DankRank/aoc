#!/usr/bin/env python3
import sys
from collections import Counter
words = input().split(', ')
input()

class NFA(dict):
    def __hash__(self):
        return id(self)

finish = NFA()
def nfa_string(s):
    nfa = finish
    for ch in s[::-1]:
        nfa = NFA({ch: {nfa}})
    return nfa

# merge all start states into the finish state
for s in words:
    alt = nfa_string(s)
    for ch in alt:
        if ch in finish:
            finish[ch] |= alt[ch]
        else:
            finish[ch] = set(alt[ch])

def run_nfa(nfa, s):
    ctr = Counter({nfa: 1})
    for ch in s:
        nctr = Counter()
        for k, v in ctr.items():
            if ch in k:
                for nk in k[ch]:
                    nctr[nk] += v
        ctr = nctr
    return ctr

count = 0
for s in sys.stdin:
    count += run_nfa(finish, s.rstrip())[finish]
print(count)
