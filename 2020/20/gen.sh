#!/bin/bash
./analyze <input.txt | sort | uniq -c | sort | sed 's/ \+/\t/g' | grep $'^\t1\t' | cut -f3 | sed 's/^/case /;s/$/:/'
