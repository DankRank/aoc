#!/usr/bin/env python3
player_hp = 100
boss_hp = int(input().split()[2])
boss_dmg = int(input().split()[1])
boss_armor = int(input().split()[1])
weaps = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armors = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

res1 = float('inf')
res2 = 0
def test(cost, dmg, armor):
    pa = max(1, dmg-boss_armor)
    ba = max(1, boss_dmg-armor)
    if (boss_hp+pa-1)//pa <= (player_hp+ba-1)//ba:
        global res1
        if cost < res1:
            res1 = cost
    else:
        global res2
        if cost > res2:
            res2 = cost

for cost1, dmg in weaps:
    for cost2, armor in armors:
        test(cost1+cost2, dmg, armor)
        for i in range(len(rings)):
            cost3, dmg1, armor1 = rings[i]
            test(cost1+cost2+cost3, dmg+dmg1, armor+armor1)
            for j in range(i+1, len(rings)):
                cost4, dmg2, armor2 = rings[j]
                test(cost1+cost2+cost3+cost4, dmg+dmg1+dmg2, armor+armor1+armor2)

print(res1)
print(res2)
