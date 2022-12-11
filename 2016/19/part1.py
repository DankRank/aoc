#!/usr/bin/env python3
elfs = int(input())
count = elfs
elf = 0
inc = 1
while count != 1:
    if count%2 == 1:
        elf = (elf-inc)%elfs
        count = count//2 + 1
        inc *= 2
    else:
        count = count//2
        inc *= 2
print(elf+1)
