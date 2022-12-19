#!/usr/bin/env pypy3
def sim(ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
    known_states = set()
    max_ore = max(clay_ore, obsidian_ore, geode_ore)
    def step(time, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode):
        if ore_r == max_ore and ore >= max_ore:
            ore = max_ore
        if clay_r == obsidian_clay and clay >= obsidian_clay:
            clay = obsidian_clay
        if obsidian_r == geode_obsidian and obsidian >= geode_obsidian:
            obsidian = geode_obsidian
        s = (time, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode)
        if s in known_states:
            return geode
        known_states.add(s)
        maxg = geode + geode_r
        if time == 24:
            return maxg
        if ore_r < max_ore:
            if ore >= ore_ore:
                maxg = max(maxg, step(time+1, ore_r+1, clay_r, obsidian_r, geode_r, ore + ore_r - ore_ore, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
        if clay_r < obsidian_clay:
            if ore >= clay_ore:
                maxg = max(maxg, step(time+1, ore_r, clay_r+1, obsidian_r, geode_r, ore + ore_r - clay_ore, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
        if obsidian_r < geode_obsidian:
            if ore >= obsidian_ore and clay >= obsidian_clay:
                maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r+1, geode_r, ore + ore_r - obsidian_ore, clay + clay_r - obsidian_clay, obsidian + obsidian_r, geode + geode_r))
        if ore >= geode_ore and obsidian >= geode_obsidian:
            maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r, geode_r+1, ore + ore_r - geode_ore, clay + clay_r, obsidian + obsidian_r - geode_obsidian, geode + geode_r))
        maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r, geode_r, ore + ore_r, clay + clay_r, obsidian + obsidian_r, geode + geode_r))
        return maxg
    return step(1, 1, 0, 0, 0, 0, 0, 0, 0)
count = 0
try:
    while True:
        line = input().split()
        count += int(line[1][:-1])*sim(int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30]))
except EOFError:
    pass
print(count)
