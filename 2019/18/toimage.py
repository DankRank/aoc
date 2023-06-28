#!/usr/bin/env python3
import sys
m = [line.rstrip() for line in sys.stdin]
def mapchr(c):
    if c == '#':
        return [0,0,0]
    if c.isupper():
        return [0,255,255]
    return [255,255,255]
im = [[mapchr(c) for c in line] for line in m]
import numpy as np
from PIL import Image
Image.fromarray(np.array(im, dtype=np.uint8), 'RGB').save('/tmp/x.png')
