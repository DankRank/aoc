#!/bin/sh
jq 'walk(if type == "object" then if any(.[]; . == "red") then {} else . end else . end)' input.txt | ./part1
