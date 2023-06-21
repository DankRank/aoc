#!/usr/bin/env python3
import sys
print(sum(int(line.rstrip())//3-2 for line in sys.stdin))
