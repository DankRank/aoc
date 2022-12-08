#!/usr/bin/env python3
boss_hp = int(input().split()[2])
boss_dmg = int(input().split()[1])

spellcost = [53, 73, 113, 173, 229]

mincost = float('inf')
def simulate(cost, hp, mana, bhp, shield, poison, recharge):
    global mincost
    if cost > mincost:
        return
    if poison > 0:
        poison -= 1
    if poison > 0:
        bhp -= 3
        if bhp <= 0:
            if cost < mincost:
                mincost = cost
            return
        poison -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1
    if recharge > 0:
        mana += 101
        recharge -= 1
    if shield > 0:
        shield -= 1
    if shield > 0:
        shield -= 1
    for i in range(5):
        if mana < spellcost[i]:
            return
        todmg = 0
        toheal = 0
        if i == 0: # Magic Missile
            todmg = 4
        elif i == 1: # Drain
            todmg = 2
            toheal = 2
        elif i == 2: # Shield
            if shield > 0:
                continue
        elif i == 3: # Poison
            if poison > 0:
                continue
        elif i == 4: # Recharge
            if recharge > 0:
                continue
        if poison > 0 or i == 3:
            todmg += 3
        if bhp - todmg <= 0:
            if cost+spellcost[i] < mincost:
                mincost = cost+spellcost[i]
            return
        tohurt = boss_dmg
        if shield > 0 or i == 2:
            tohurt = max(1, tohurt-7)
        tohurt += 1
        if hp+toheal-tohurt <= 0:
            continue
        simulate(cost+spellcost[i], hp+toheal-tohurt, mana-spellcost[i], bhp-todmg, 6 if i == 2 else shield, 6 if i == 3 else poison, 5 if i == 4 else recharge)

simulate(0, 50-1, 500, boss_hp, 0, 0, 0)
print(mincost)
