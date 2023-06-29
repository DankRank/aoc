#!/usr/bin/env python3
from intcode import *
def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
m = {}
vm = IntcodeVM(parsetext(input()))
vm.text[0] = 2
score = 0
while not vm.halted:
    vm.run()
    while len(vm.outq):
        x = vm.outq.pop(0)
        y = vm.outq.pop(0)
        v = vm.outq.pop(0)
        if x == -1 and y == 0:
            score = v
        else:
            if v == 3:
                paddlex = x
            elif v == 4:
                ballx = x
            m[(x,y)] = v
    #minx = min(m.keys(), key=lambda x: x[0])[0]
    #maxx = max(m.keys(), key=lambda x: x[0])[0]
    #miny = min(m.keys(), key=lambda x: x[1])[1]
    #maxy = max(m.keys(), key=lambda x: x[1])[1]
    #print('\033[H')
    #for y in range(miny, maxy+1):
    #    line = []
    #    for x in range(minx, maxx+1):
    #        line.append(str(m[(x,y)]))
    #    print(''.join(line))
    #print(score)
    vm.inq.append(int(sgn(ballx-paddlex)))
print(score)
