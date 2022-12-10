#!/usr/bin/env python3
mapp = {
    '...': '.',
    '..^': '^',
    '.^.': '.',
    '^..': '^',
    '.^^': '^',
    '^.^': '.',
    '^^.': '^',
    '^^^': '.',
}
line = input()
count = line.count('.')
for i in range(399999):
    line = '.'+line+'.'
    line = ''.join(mapp[line[i:i+3]] for i in range(len(line)-2))
    count += line.count('.')
print(count)

