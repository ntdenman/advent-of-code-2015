# Just putting the input right here b/c parsing blocks seems like effort
# Added a None armor and None accessory

in_weps = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

in_arm = """None    0   0   0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

in_accs = """None   0   0   0
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""

boss_stats = [109,8,2]
# hp, atk, def

def can_win(player_stats, boss_stats):
    # boss net dmg to player per round
    boss_dpr = max(boss_stats[1]-player_stats[2], 1)

    # ceiling division
    player_lifespan = -(player_stats[0] // -boss_dpr)

    # et. v. v.
    player_dpr = max(player_stats[1]-boss_stats[2], 1)
    boss_lifespan = -(boss_stats[0] // -player_dpr)

    # player alwyas goes first
    # so will win ties
    return player_lifespan >= boss_lifespan

weps = []
for line in in_weps.split("\n"):
    data = line.split()
    weps.append([int(data[1]), int(data[2])])

arms = []
for line in in_arm.split("\n"):
    data = line.split()
    arms.append([int(data[1]), int(data[3])])

accs = []
for line in in_accs.split("\n"):
    data = line.split()
    accs.append([int(data[1]), int(data[2]), int(data[3])])

costs = []

player_stats = [100,0,0]
# hp, atk, def

# loop over weapon choices, as we must choose exactly one
for wep in weps:
    # over armours, with 'None' as an option
    for arm in arms:
        # over accessories, with 'None' as an option
        for acc1 in accs:
            # over second accessory, with 'None' as an option 
            # and also a uniqueness condition
            for acc2 in accs:
                test_gold = wep[0] + arm[0] + acc1[0]
                test_stats = player_stats
                test_stats[1] = wep[1] + acc1[1]
                test_stats[2] = arm[1] + acc1[2]

                if not acc2 == acc1:
                    # can't get two of the same thing
                    test_stats[1] += acc2[1]
                    test_stats[2] += acc2[2]
                    test_gold += acc2[0]

                # run the fight either way; will duplicate the no-acc2-case but not too badly
                if can_win(test_stats, boss_stats):
                    costs.append(test_gold)

print(min(costs))

