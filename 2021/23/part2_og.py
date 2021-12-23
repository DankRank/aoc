#!/usr/bin/env python3
# originally solved at 36:21, except I messed up the second line (8*A), and had to write an actual solution :sob:
A = 1
B = 10
C = 100
D = 1000
print(sum([
    #############
    #...........#
    ###D#C#A#B###
      #D#C#B#A#
      #D#B#A#C#
      #C#D#A#B#
      #########
    9*B,
    9*A,
    5*C,
    5*B,
    11*D,
    11*D,
    11*D,
    #############
    #BA.......BC#
    ###.#C#A#.###
      #.#C#B#D#
      #.#B#A#D#
      #C#D#A#D#
      #########
    9*C,
    5*A,
    8*A,
    7*B,
    9*A,
    9*A,
    5*C,
    6*C,
    6*C,
    #############
    #BB.......BC#
    ###A#.#.#.###
      #A#.#C#D#
      #A#B#C#D#
      #A#D#C#D#
      #########
    4*B,
    9*D,
    5*B,
    6*B,
    6*B,
    6*B,
    5*C,
]))
