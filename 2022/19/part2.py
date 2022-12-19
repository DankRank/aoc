#!/usr/bin/env pypy3
import gc
def sim(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
    max_ore = max(clay_ore, obsidian_ore, geode_ore)
    prev_states = set()
    next_states = {(1, 0, 0, 0, 0, 0, 0, 0)}
    maxg = 0
    time = 0
    while len(next_states) > 0:
        prev_states, next_states = next_states, set()
        prev_states = list(prev_states)
        #print('collecting gargbage')
        gc.collect()
        #print('collected')
        time += 1
        while len(prev_states) > 0:
            ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode = prev_states.pop()
            if ore_r == max_ore and ore >= max_ore:
                ore = max_ore
            if clay_r == obsidian_clay and clay >= obsidian_clay:
                clay = obsidian_clay
            if obsidian_r == geode_obsidian and obsidian >= geode_obsidian:
                obsidian = geode_obsidian
            maxg = max(maxg, geode + geode_r)
            #if len(next_states)>0 and len(next_states)%1000000 == 0:
            #    print(time, len(next_states))
            if time < 32:
                if ore_r < max_ore and ore >= ore_ore:
                    next_states.add((ore_r+1, clay_r, obsidian_r, geode_r, ore + ore_r - ore_ore, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
                if clay_r < obsidian_clay and ore >= clay_ore:
                    next_states.add((ore_r, clay_r+1, obsidian_r, geode_r, ore + ore_r - clay_ore, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
                if obsidian_r < geode_obsidian and ore >= obsidian_ore and clay >= obsidian_clay:
                    next_states.add((ore_r, clay_r, obsidian_r+1, geode_r, ore + ore_r - obsidian_ore, clay + clay_r - obsidian_clay, obsidian + obsidian_r, geode + geode_r))
                if ore >= geode_ore and obsidian >= geode_obsidian:
                    next_states.add((ore_r, clay_r, obsidian_r, geode_r+1, ore + ore_r - geode_ore, clay + clay_r, obsidian + obsidian_r - geode_obsidian, geode + geode_r))
                next_states.add((ore_r, clay_r, obsidian_r, geode_r, ore + ore_r, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
    #print(maxg)
    return maxg
count = 1
try:
    while True:
        line = input().split()
        if int(line[1][:-1]) < 3:
            count *= sim(int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30]))
except EOFError:
    pass
print(count)
