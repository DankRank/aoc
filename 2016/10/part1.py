#!/usr/bin/env python3
import functools
import operator
bots = {}
outputs = {}
def get_bot(i):
    if i not in bots:
        bots[i] = {'in': [], 'lo': None, 'hi': None, 'decided': False}
    return bots[i]
def get_output(i):
    if i not in outputs:
        outputs[i] = {'in': []}
    return outputs[i]
try:
    while True:
        line = input().split()
        if line[0] == 'value':
            get_bot(int(line[5]))['in'].append(int(line[1]))
        else:
            bot = get_bot(int(line[1]))
            lo = int(line[6])
            hi = int(line[11])
            bot['lo'] = get_bot(lo) if line[5] == 'bot' else get_output(lo)
            bot['hi'] = get_bot(hi) if line[10] == 'bot' else get_output(hi)
except EOFError:
    pass
undecided = len(bots)
while undecided > 0:
    undecided_at_start = undecided
    for i, bot in bots.items():
        if not bot['decided'] and len(bot['in']) == 2:
            bot['hi']['in'].append(max(bot['in']))
            bot['lo']['in'].append(min(bot['in']))
            bot['decided'] = True
            undecided -= 1
    assert undecided != undecided_at_start
print(*(i for i, bot in bots.items() if sorted(bot['in']) == [17, 61]))
print(functools.reduce(operator.mul, (outputs[i]['in'][0] for i in range(3))))
