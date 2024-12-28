#!/usr/bin/env python3
line = [ord(x) for x in input()]

def reduce(line):
    changed = True
    l = len(line)
    while changed:
        changed = False
        i = 0
        j = 0
        while i < l:
            if i < l-1 and line[i]^line[i+1] == 0x20:
                i += 2
                while j and i < l and line[j-1]^line[i] == 0x20:
                    i += 1
                    j -= 1
                changed = True
            else:
                line[j] = line[i]
                i += 1
                j += 1
        l = j
    del line[l:]
    return line

print(len(reduce(line.copy())))

minlen = float('inf')
for i in range(ord('A'), ord('Z')+1):
    nline = [ch for ch in line if ch != i if ch != i^0x20]
    nlen = len(reduce(nline))
    if nlen < minlen:
        minlen = nlen
print(minlen)
