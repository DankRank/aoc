#!/usr/bin/env python3
import sys
import re
import os
pattern = '|'.join(input().split(', '))
input()
with os.popen(f'grep -E \'^({pattern})*$\' | wc -l', 'w') as f:
    for line in sys.stdin:
        f.write(line)
