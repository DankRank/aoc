#!/usr/bin/env python3
import sys, re
def parse(line):
    m = re.search(r'^(.*) \(contains (.*)\)$', line)
    if m is None:
        raise TypeError
    ingredients = set(m.group(1).split(' '))
    allergens = set(m.group(2).split(', '))
    return ingredients, allergens
foods = [parse(line.rstrip()) for line in sys.stdin]
all_ingredients = {c for a,b in foods for c in a}
all_allergens = {c for a,b in foods for c in b}
undecided = {allergen:
        all_ingredients.intersection(*(a for a,b in foods if allergen in b))
        for allergen in all_allergens}
decided = {}
while len(undecided) > 0:
    new_k = set()
    new_v = set()
    for k,vset in undecided.items():
        if len(vset) == 1:
            v = next(iter(vset))
            new_k.add(k)
            new_v.add(v)
            decided[k] = v
    old_len = len(undecided)
    undecided = {k:v.difference(new_v) for k,v in undecided.items() if k not in new_k}
    assert old_len != len(undecided)
allergen_ingredients = set(decided.values())
# part 1
print(len([c for a,b in foods for c in a if c not in allergen_ingredients]))
# part 2
print(','.join([v for k,v in sorted(decided.items())]))
