import random
import numpy as np
import copy

# Stats arein order:
# HP, MANA, DMG, DEF
init_boss_stats = [13, 0, 8, 0]
#init_boss_stats = [71,0,10,0]
init_player_stats = [10, 250, 0, 0]
#init_player_stats = [50,500,0,0]

# Assuming this is enough? 
min_spent_to_win = 99999

# Loading up the list of spells
# Data structure for the spells is as follows:
# Each spell is an entry within the list of spells
# which has a mana cost, duration (0 for instants), and effects
# expressed as list of deltas to boss stats and your stats
# for the effect on initial cast, effect each turn, effect on end

spells = [
        {"name": "Magic Missile", 
            "cost": 53,
            "effect": [[[0,0,0,0],[-4,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]]],
            "duration": 0},
        {"name": "Drain", 
            "cost": 73,
            "effect": [[[2,0,0,0],[-2,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]]],
            "duration": 0},
        {"name": "Shield", 
            "cost": 113,
            "effect": [[[0,0,0,7],[0,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]],
                       [[0,0,0,-7],[0,0,0,0]]],
            "duration": 6},
        {"name": "Poison", 
            "cost": 173,
            "effect": [[[0,0,0,0],[0,0,0,0]],
                       [[0,0,0,0],[-3,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]]],
            "duration": 6},
        {"name": "Recharge", 
            "cost": 229,
            "effect": [[[0,0,0,0],[0,0,0,0]],
                       [[0,101,0,0],[0,0,0,0]],
                       [[0,0,0,0],[0,0,0,0]]],
            "duration": 5}
        ]

# So what do?
# Start fight with some stats
# if it can be cast, 

def apply_effects(player_status, boss_status, effects):

    # applies current effects
    # which are expressed as [effect, remaining_duration]
    print("pre-application", player_status, boss_status)
    for effect in effects:
        player_status = np.add(player_status, effect[0][1][0])
        boss_status = np.add(boss_status, effect[0][1][1])
        print("post-application", player_status, boss_status)

        # count down durations
        effect[1] -= 1

        # if effect expired
        if effect[1] == 0: #termination effects
            player_status = np.add(player_status, effect[0][2][0])
            boss_status = np.add(boss_status, effect[0][2][1])
            # no longer applied
            effects.remove(effect)
    return

def check_win(boss_stats, mana_spent, min_spend):
    # See if boss perished
    if boss_stats[0] <= 0:
        print("won at", mana_spent)
        if mana_spent < min_spend:
            min_spend = mana_spent
            print("new min", min_spend)
        return True
    else:
        return False


def have_turns(player_status, boss_status, effects_in, mana_spent, min_spent_to_win, cast_chain):

    # copy vars for this branch
    player_status_new = copy.copy(player_status)
    boss_status_new = copy.copy(boss_status)
    effects = copy.copy(effects_in)
    mana_spent_new = copy.copy(mana_spent)
    cast_chain_new = copy.copy(cast_chain)

    print("-> begin turn with chain", cast_chain_new)

    # apply any current effects at start of player's turn
    for effect in effects:
        player_status_new = np.add(player_status_new, effect[0][1][0])
        boss_status_new = np.add(boss_status_new, effect[0][1][1])
        effect[1] -= 1
        if effect[1] == 0: #termination effects
            player_status_new = np.add(player_status_new, effect[0][2][0])
            boss_status_new = np.add(boss_status_new, effect[0][2][1])
            # no longer applied
            effects.remove(effect)
 
    # if the player just won, end this branch
    if check_win(boss_status_new, mana_spent_new, min_spent_to_win):
        return

    # I am explicitly assuming we'll find a winning fight
    # prior to hitting limits due to an endless fight
    # but randomizing spell selection seems reasonable
    #random.shuffle(spells)

    for spell in spells:
        player_status_tmp = copy.copy(player_status_new)
        boss_status_tmp = copy.copy(boss_status_new)
        effects_tmp = copy.copy(effects)
        mana_spent_tmp = copy.copy(mana_spent_new)
        cast_chain_tmp = copy.copy(cast_chain_new)

        print("test", spell["name"], player_status_tmp, boss_status_tmp, "prev: ", cast_chain_tmp)

        if spell["cost"] > player_status_tmp[1]: # can't afford it
            continue
        else:
            is_applied = False
            for eft in effects_tmp:
                if spell["effect"] == eft[0]: # already applied
                    print("already applied")
                    is_applied = True
            if is_applied:
                continue

            # can cast this spell
            else:
                # Spend mana, apply effects
                mana_spent_tmp += spell["cost"]
                player_status_tmp[1] -= spell["cost"]
                player_status_tmp = np.add(player_status_tmp, spell["effect"][0][0])
                print("effect on boss", spell["effect"][0][1], boss_status_tmp)
                boss_status_tmp = np.add(boss_status_tmp, spell["effect"][0][1])

                print(spell["name"],spell["duration"], mana_spent_tmp, player_status_tmp, boss_status_tmp)

                # spells which linger are added to active effects
                if spell["duration"] > 0:
                    effects_tmp.append([spell["effect"], spell["duration"]])
                    print("appended", effects_tmp)

            # if this spell won the fight, no new branch with this spell
            if check_win(boss_status_tmp, mana_spent_tmp, min_spent_to_win):
                continue
            else:
                # boss then has a turn
                # apply effects
                for effect in effects_tmp:
                   player_status_tmp = np.add(player_status_tmp, effect[0][1][0])
                   boss_status_tmp = np.add(boss_status_tmp, effect[0][1][1])

                   effect[1] -= 1

                   if effect[1] == 0: #termination effects
                       player_status_tmp = np.add(player_status_tmp, effect[0][2][0])
                       boss_status_tmp = np.add(boss_status_tmp, effect[0][2][1])
                       # no longer applied
                       print("expired")
                       effects.remove(effect)

                print("after boss turn start", player_status_tmp, boss_status_tmp)

                # did boss die at the beginning of their turn?
                if check_win(boss_status_tmp, mana_spent_tmp, min_spent_to_win):
                    continue
                else:
                    # boss does damage to player
                    boss_dmg = max(1, boss_status_tmp[2] - player_status_tmp[3])
                    player_status_tmp[0] -= boss_dmg
                    print("post boss turn, new stats:", player_status_tmp, boss_status_tmp)

                    if player_status_tmp[0] <= 0: #lose
                        print("lost")
                        continue
                    else:
                        cast_chain_tmp.append(spell["name"])
                        # reached the end of the two turns with both still alive
                        # so time to take another two turns on this branch
                        have_turns(player_status_tmp, boss_status_tmp, effects_tmp, mana_spent_tmp, min_spent_to_win, cast_chain_tmp)
    print("== end of branch", cast_chain_new)

have_turns(init_player_stats, init_boss_stats, [], 0, min_spent_to_win, [])

print(min_spent_to_win)
