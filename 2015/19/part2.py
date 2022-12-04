#!/usr/bin/env python3
# Sort the rules by length of the right side
# It becomes apparent that they follow one of four patterns:
# t => a b
# t => a Rn b Ar
# t => a Rn b Y c Ar
# t => a Rn b Y c Y d Ar
# Also, Rn Y and Ar (and also C, the first symbol in the input) are the only terminals.
# Another thing to note is that for "abc" it doesn't matter if we first fold ab or bc,
# because an answer does exist (I sure hope it does), it will eventually fold into a
# single nonterminal. It takes the same amount of steps to fold it either way, so
# WLOG we can consider case where everything is folded into the first nonterm.
# For Rn/Ar sequences we first fold b/c/d into one token, then we fold the whole thing
# into the a. Because there are terminals sprinkled between b/c/d, the order of eval
# doesn't matter here either.
#
# `a b` folds 1 terminal in 1 step
# `a Rn b Ar` folds 3 in 1
# `a Rn b Y c Ar` folds 5 in 1
# `a Rn b Y c Y d Ar` folds 7 in 1
#
# So in general, each token in the input costs us 1 step unless it's:
# - the initial token
# - Rn or Ar
# - Y or the token that follows a Y
import re
try:
    while True:
        line = input()
        if line == '':
            pattern = input()
            break
except EOFError:
    pass
toks = re.sub('[A-Z]', r' \g<0>', pattern).split()
print(len(toks) - 1 - sum(1 for t in toks if t == 'Rn' or t == 'Ar') - 2*sum(1 for t in toks if t == 'Y'))
