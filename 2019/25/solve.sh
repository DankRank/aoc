#!/bin/sh
cat input.txt solve.txt | ./part1.py -i | sed -n '/TRYING/h;/You may proceed/{g;p;q}'
