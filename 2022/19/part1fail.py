#!/usr/bin/env python3
def sim(index, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
    max_ore = max(clay_ore, obsidian_ore, geode_ore)
    def step(time, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode):
        ore += ore_r
        clay += clay_r
        obsidian += obsidian_r
        geode += geode_r
        maxg = geode
        if time == 24:
            return geode
        taken_pass = False
        if ore - ore_r >= geode_ore and obsidian - obsidian_r >= geode_obsidian:
            maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r, geode_r+1, ore - geode_ore, clay, obsidian - geode_obsidian, geode))
        elif ore - ore_r >= obsidian_ore and clay - clay_r >= obsidian_clay:
            maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r+1, geode_r, ore - obsidian_ore, clay - obsidian_clay, obsidian, geode))
        elif ore - ore_r >= clay_ore:
            maxg = max(maxg, step(time+1, ore_r, clay_r+1, obsidian_r, geode_r, ore - clay_ore, clay, obsidian, geode))
        else:
            taken_pass = True
            maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode))

        if ore_r < max_ore:
            if ore - ore_r >= ore_ore:
                maxg = max(maxg, step(time+1, ore_r+1, clay_r, obsidian_r, geode_r, ore - ore_ore, clay, obsidian, geode))
            elif not taken_pass:
                maxg = max(maxg, step(time+1, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode))
        return maxg
    x = step(1, 1, 0, 0, 0, 0, 0, 0, 0)
    print(x)
    return x*index
count = 0
try:
    while True:
        line = input().split()
        count += sim(int(line[1][:-1]), int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30]))
except EOFError:
    pass
print(count)
