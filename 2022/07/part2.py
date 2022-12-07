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

dirlist = []
def calcsize(cdir):
    total = 0
    for v in cdir['dirs'].values():
        if 'totalsize' not in v:
            calcsize(v)
        total += v['totalsize']
    total += sum(cdir['files'].values())
    cdir['totalsize'] = total
    global dirlist
    dirlist.append(total)
calcsize(rootdir)
dirlist.sort()

need = 30000000 - (70000000 - rootdir['totalsize'])
for i in dirlist:
    if i >= need:
        print(i)
        break
