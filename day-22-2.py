import numpy as np
import copy

# Total re-write of this problem:
# Previous attempt was too ambitious, 
# aiming to support arbitrary spell selection
# and effects on the boss

# New attempt will hardcode much of the effects
# otherwise I'd be here all day

# Initial Conditions
pl_stats = {"hp" : 50,
            "mana": 500,
            "def": 0 }

bs_stats = {"hp": 71,
            "dmg": 10}

timers = {"shield": 0,
          "poison": 0,
          "recharge": 0}

mana_costs = {"missile": 53, 
                "drain": 73,
                "shield":113,
                "poison":173,
                "recharge":229}

mana_spent = 0
wins = [99999]

# Defining a new function which takes the player & boss turns
# it directly modifies the variables of interest

def take_turns(pl_stats, bs_stats, timers, mana_costs, mana_spent, wins, casts):
    # begin with the player's turn

    # Hardmode:
    pl_stats["hp"] -= 1
    if pl_stats["hp"] <= 0:
        #print("Loss")
        return wins 

    # first, evaluate any ongoing effects:
    if timers["shield"] > 0:
        timers["shield"] -= 1
        if timers["shield"] == 0:

            pl_stats["def"] = 0

    if timers["poison"] > 0:
        bs_stats["hp"] -= 3
        timers["poison"] -= 1

    if timers["recharge"] > 0:
        pl_stats["mana"] += 101
        timers["recharge"] -= 1

    # See if we just won
    if bs_stats["hp"] <= 0:
        #print("-- Won with spend:", mana_spent)
        wins.append(mana_spent)
        return wins

    # otherwise, player's turn:

    for spell in mana_costs.keys():
        # Create copy of the current state as of the choice of spell
        ps_new = copy.copy(pl_stats)
        bs_new = copy.copy(bs_stats)
        tm_new = copy.copy(timers)
        ms_new = copy.copy(mana_spent)
        cast_new = copy.copy(casts)
        cast_new.append(spell)

        if ps_new["mana"] < mana_costs[spell]:
            #print("Can't afford that")
            continue

        #print("Begin casts for branch", cast_new)

        if spell in tm_new:
            if tm_new[spell] > 0:
                #print("Timer still on")
                continue

        if spell == "missile":
            ms_new += 53
            ps_new["mana"] -= 53
            bs_new["hp"] -= 4
    
        elif spell == "drain":
            ms_new += 73
            ps_new["mana"] -= 73
            bs_new["hp"] -= 2
            ps_new["hp"] += 2
     
        elif spell == "shield":
            ms_new += 113
            ps_new["mana"] -= 113
            ps_new["def"] = 7
            tm_new[spell] = 6

        elif spell == "poison":
            ms_new += 173
            ps_new["mana"] -= 173
            tm_new[spell] = 6

        elif spell == "recharge":
            ms_new += 229
            ps_new["mana"] -= 229
            tm_new[spell] = 5

        if len(wins) > 0:
            if ms_new > min(wins):
                #print("Spent more than current best, can abandon this branch")
                continue

        #print("Post-player-cast stats:", ps_new, bs_new)

        # Boss has a turn:

        # First, apply effects:
        if tm_new["shield"] > 0:
            tm_new["shield"] -= 1
            if tm_new["shield"] == 0:
                ps_new["def"] = 0
    
        if tm_new["poison"] > 0:
            bs_new["hp"] -= 3
            tm_new["poison"] -= 1
    
        if tm_new["recharge"] > 0:
            ps_new["mana"] += 101
            tm_new["recharge"] -= 1

        # See if we just won
        if bs_new["hp"] <= 0:
            #print("--- Won with spend:", ms_new)
            wins.append(ms_new)
            continue

        #print("Pre-boss-atk stats:", ps_new, bs_new)

        # Then boss attacks:
        ps_new["hp"] -= max(1, bs_new["dmg"] - ps_new["def"])

        #print("Post-boss-atk stats:", ps_new, bs_new)

        if ps_new["hp"] <= 0:
            #print("Loss")
            continue
        
        # Made it to the end of the turn without either winning or losing
        # So we will start a new set of turns from this point

        wins = take_turns(ps_new, bs_new, tm_new, mana_costs, ms_new, wins, cast_new)
    
    return wins

wins = take_turns(pl_stats, bs_stats, timers, mana_costs, mana_spent, wins, [])

if len(wins) > 0:
    print("Lowest winning spend:", min(wins))
else:
    print("couldn't win")
