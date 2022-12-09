#!/usr/bin/env python3
floors = [
    ['TG', 'TM', 'PG', 'SG'],
    ['PM', 'SM'],
    ['pG', 'pM', 'RG', 'RM'],
    [],
]
floor = 0
steps = 0
def check():
    print(floor, floors)
    for f in floors:
        assert not(any(x[1] == 'G' for x in f) and any(x[1] == 'M' and not x[0]+'G' in f for x in f))
def moveup(a, b=None):
    global floor
    global steps
    assert a is not None
    assert b is None or a[0] == b[0] or a[1] == b[1]
    assert floor < 3
    floors[floor].remove(a)
    floors[floor+1].append(a)
    if b is not None:
        floors[floor].remove(b)
        floors[floor+1].append(b)
    floor += 1
    steps += 1
    check()
def movedown(a, b=None):
    global floor
    global steps
    assert a is not None
    assert b is None or a[0] == b[0] or a[1] == b[1]
    assert floor > 0
    floors[floor].remove(a)
    floors[floor-1].append(a)
    if b is not None:
        floors[floor].remove(b)
        floors[floor-1].append(b)
    floor -= 1
    steps += 1
    check()

moveup('PG', 'SG') # the only possible move
moveup('SG', 'SM')
# the classic solution without last step
moveup('SG', 'SM')
movedown('SG')
moveup('RM', 'pM')
movedown('SM')
moveup('RG','pG')
movedown('RG', 'RM')
moveup('SG', 'RG')
movedown('pM')
moveup('SM', 'pM')
movedown('RG')
# half-solve floor 1
movedown('RG')
movedown('RG')
moveup('RG', 'TG')
moveup('RG', 'TG')
moveup('RG', 'TG')
# half-solve floor 2
movedown('RG')
movedown('RG')
moveup('RG', 'PG')
moveup('RG', 'PG')
# solve Ms
movedown('SM')
movedown('SM')
movedown('SM')
moveup('SM', 'TM')
moveup('SM', 'TM')
movedown('SM')
moveup('SM', 'PM')
moveup('SM', 'TM')
movedown('SM')
moveup('SM', 'PM')
movedown('SM')
moveup('SM', 'RM')

print(floor, floors)
assert all(len(f) == 0 for f in floors[:-1])
print(steps)
