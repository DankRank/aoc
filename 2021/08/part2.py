#!/usr/bin/env python3
from itertools import chain
count = 0
try:
    while True:
        inputs, outputs = map(lambda x: list(map(frozenset, x.split(' '))), input().split(' | '))
        known = [False]*10
        solved = {}
        def mark(s, n):
            known[n] = s
            solved[s] = n
        while not all(x in solved for x in outputs):
            for s in chain(inputs, outputs):
                if s not in solved:
                    if len(s) == 2:
                        # 1
                        mark(s, 1)
                    elif len(s) == 3:
                        # 7
                        mark(s, 7)
                    elif len(s) == 4:
                        # 4
                        mark(s, 4)
                    elif len(s) == 5:
                        # 2, 3, 5
                        #        2
                        # 1, 7 < 3 <    9
                        #        5 < 6, 9
                        if known[3] and known[5]:
                            mark(s, 2)
                        elif known[2] and known[5]:
                            mark(s, 3)
                        elif known[2] and known[3]:
                            mark(s, 5)
                        elif known[1] and known[1] < s:
                            mark(s, 3)
                        elif known[7] and known[7] < s:
                            mark(s, 3)
                        elif known[6] and s < known[6]:
                            mark(s, 5)
                        elif known[9] and not s < known[9]:
                            mark(s, 2)
                        # at this point checks involving two negatives can be made, e.g.
                        # elif (known[1] or known[7]) and known[6]:
                        #     mark(s, 2)
                        # I didn't need them for my input tho
                    elif len(s) == 6:
                        # 6, 9, 0
                        #          5    < 6
                        # 1, 3, 4, 5, 7 < 9
                        # 1,          7 < 0
                        if known[6] and known[9]:
                            mark(s, 0)
                        elif known[0] and known[9]:
                            mark(s, 6)
                        elif known[0] and known[6]:
                            mark(s, 9)
                        elif known[1] and not known[1] < s:
                            mark(s, 6)
                        elif known[3] and known[3] < s:
                            mark(s, 9)
                        elif known[4] and known[4] < s:
                            mark(s, 9)
                        elif known[5] and not known[5] < s:
                            mark(s, 0)
                        elif known[7] and not known[7] < s:
                            mark(s, 6)
                        # remarks above apply here as well
                    elif len(s) == 7:
                        # 8
                        mark(s, 8)
        count += int("".join(map(lambda x: str(solved[x]), outputs)))
except EOFError:
    pass
print(count)
