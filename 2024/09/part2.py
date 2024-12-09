#!/usr/bin/env python3
line = [int(x) for x in input()]
assert len(line) % 2
i = 0
j = len(line)-1
rle = []
for i in range(len(line)):
    if i%2 == 0:
        if line[i]:
            rle.append((i//2, line[i]))
    else:
        if line[i]:
            rle.append((None, line[i]))
minseen = len(line)//2 + 1
firsti = 0
j = len(rle)-1
while j >= 0:
    if rle[j][0] is not None and rle[j][0] < minseen:
        minseen = rle[j][0]
        while firsti < j and rle[firsti][0] is not None:
            firsti += 1
        i = firsti
        while i < j:
            if rle[i][0] is None and rle[i][1] >= rle[j][1]:
                if rle[i][1] == rle[j][1]:
                    rle[i] = rle[j]
                else:
                    rle[i] = (None, rle[i][1] - rle[j][1])
                    rle.insert(i, rle[j])
                    j += 1
                rle[j] = (None, rle[j][1])
                # merge with the one after
                if j+1 < len(rle) and rle[j+1][0] is None:
                    rle[j] = (None, rle[j][1] + rle[j+1][1])
                    del rle[j+1]
                # merge with the one before
                if j and rle[j-1][0] is None:
                    rle[j-1] = (None, rle[j-1][1] + rle[j][1])
                    del rle[j]
                    j -= 1
                break
            i += 1
    j -= 1
count = 0
pos = 0
for fileid, rep in rle:
    if fileid is not None:
        count += fileid*(pos*rep + rep*(rep-1)//2)
    pos += rep
print(count)
