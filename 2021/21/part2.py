#!/usr/bin/env python3
p1 = int(input().split()[-1])-1
p2 = int(input().split()[-1])-1

roll_copies = [
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1)
]

def step(p1, p2, s1, s2, copies):
    win1 = 0
    win2 = 0
    for r1, c1 in roll_copies:
        np1 = (p1 + r1) % 10
        ns1 = s1 + np1 + 1
        if ns1 >= 21:
            win1 += copies * c1
            continue
        for r2, c2 in roll_copies:
            np2 = (p2 + r2) % 10
            ns2 = s2 + np2 + 1
            if ns2 >= 21:
                win2 += copies * c1 * c2
                continue
            nwin1, nwin2 = step(np1, np2, ns1, ns2, copies * c1 * c2)
            win1 += nwin1
            win2 += nwin2
    return win1, win2

print(max(step(p1, p2, 0, 0, 1)))
