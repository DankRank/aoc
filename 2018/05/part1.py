#!/usr/bin/env python3
line = [ord(x) for x in input()]

def reduce(line):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(line)-1:
            if line[i]^line[i+1] == 0x20:
                del line[i:i+2]
                changed = True
            else:
                i += 1
    return line

print(len(reduce(line.copy())))

minlen = float('inf')
for i in range(ord('A'), ord('Z')+1):
    nline = [ch for ch in line if ch != i if ch != i^0x20]
    nlen = len(reduce(nline))
    if nlen < minlen:
        minlen = nlen
print(minlen)
