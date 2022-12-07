#!/usr/bin/env python3
rootdir = {'dirs':{}, 'files':{}}
curdir = rootdir
try:
    while True:
        line = input().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    curdir = rootdir
                elif line[2] == '..':
                    curdir = curdir['parent']
                else:
                    curdir = curdir['dirs'][line[2]]
            # we don't care about $ ls
        else:
            size, name = line
            if size == 'dir':
                assert name not in curdir['dirs']
                curdir['dirs'][name] = {'dirs':{}, 'files':{}, 'parent':curdir}
            else:
                curdir['files'][name] = int(size)
except EOFError:
    pass

res = 0
def calcsize(cdir):
    total = 0
    for v in cdir['dirs'].values():
        if 'totalsize' not in v:
            calcsize(v)
        total += v['totalsize']
    total += sum(cdir['files'].values())
    cdir['totalsize'] = total
    if total <= 100000:
        global res
        res += total
calcsize(rootdir)
print(res)
