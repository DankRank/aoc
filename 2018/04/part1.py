#!/usr/bin/env python3
import sys
from collections import Counter

log = []
for line in sys.stdin:
    line = line.rstrip().split()
    ts = f'{line[0]} {line[1]}'[1:-1]
    op = line[2]
    if op == 'Guard':
        gid = int(line[3].removeprefix('#'))
        log.append((ts, op, gid))
    else:
        log.append((ts, op))

log.sort()

log2 = []
gids = set()
gid = None
for line in log:
    if line[1] == 'Guard':
        gid = line[2]
        gids.add(gid)
    else:
        date, time = line[0].split()
        h, m = (int(i) for i in time.split(':'))
        assert h == 0
        line = (date, m, line[1], gid)
        log2.append(line)

log3 = []
for (d1, m1, op1, gid1), (d2, m2, op2, gid2) in zip(log2[::2], log2[1::2]):
    assert d1 == d2
    assert op1 == 'falls'
    assert op2 == 'wakes'
    assert gid1 == gid2
    assert m1 < m2
    log3.append((gid1, m1, m2))

gstats = {i: Counter() for i in gids}
for gid, m1, m2 in log3:
    gstats[gid].update(range(m1, m2))
topgid = max(gstats.items(), key=lambda x: x[1].total())[0]
topmin = gstats[topgid].most_common(1)[0][0]
print(topgid*topmin)

mstats = {}
for gid, stats in gstats.items():
    if len(stats):
        m, times = stats.most_common(1)[0]
        if m not in mstats or times > mstats[m][0]:
            mstats[m] = (times, gid)
topmin = max(mstats.items(), key=lambda x: x[1][0])[0]
topgid = mstats[topmin][1]
print(topgid*topmin)
