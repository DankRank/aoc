#!/usr/bin/env python3
count = 0
try:
    while True:
        inputs, outputs = map(lambda x: x.split(' '), input().split(' | '))
        for i in map(len, outputs):
            if i in [2, 4, 3, 7]:
                count += 1
except EOFError:
    pass
print(count)
