#!/usr/bin/env python3
A = 1
B = 10
C = 100
D = 1000
print(sum([
    #############
    #...........#
    ###D#C#A#B###
      #C#D#A#B#
      #########
    3*B,
    3*B,
    9*D,
    7*A,
    7*A,
    5*C,
    7*D,
    7*C,
    #############
    #AA.......BB#
    ###.#.#C#D###
      #.#.#C#D#
      #########
    3*A,
    3*A,
    6*B,
    6*B
]))
