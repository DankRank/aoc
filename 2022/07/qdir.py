#!/usr/bin/env python3
dirstack = []
print('[qdirstat 1.0 cache file]')
try:
    while True:
        line = input().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    dirstack = []
                    print(f'D /{"/".join(dirstack)}\t0\t1670389200')
                elif line[2] == '..':
                    dirstack.pop()
                else:
                    dirstack.append(line[2])
                    print(f'D /{"/".join(dirstack)}\t0\t1670389200')
            # we don't care about $ ls
        else:
            size, name = line
            if size != 'dir':
                print(f'F\t{name}\t{int(size)}\t1670389200')
except EOFError:
    pass
