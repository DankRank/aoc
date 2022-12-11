#!/usr/bin/env python3
monkeys = []
try:
    while True:
        line = input().split()
        if len(line) == 0:
            pass
        elif line[0] == 'Monkey':
            monkey = {'count': 0}
            monkeys.append(monkey)
        elif line[0] == 'Starting':
            monkey['items'] = [int(s.rstrip(',')) for s in line[2:]]
        elif line[0] == 'Operation:':
            if line[4] == '+':
                monkey['op'] = lambda a,b=int(line[5]): a+b
            elif line[4] == '*':
                if line[5] != 'old':
                    monkey['op'] = lambda a,b=int(line[5]): a*b
                else:
                    monkey['op'] = lambda a: a*a
        elif line[0] == 'Test:':
            monkey['div'] = int(line[3])
        elif line[0] == 'If':
            if line[1] == 'true:':
                monkey['passt'] = int(line[5])
            else:
                monkey['passf'] = int(line[5])
except EOFError:
    pass

for i in range(20):
    for monkey in monkeys:
        for item in monkey['items']:
            item = monkey['op'](item)//3
            if item % monkey['div'] == 0:
                monkeys[monkey['passt']]['items'].append(item)
            else:
                monkeys[monkey['passf']]['items'].append(item)
        monkey['count'] += len(monkey['items'])
        monkey['items'] = []

a,b = sorted((x['count'] for x in monkeys), reverse=True)[:2]
print(a*b)
