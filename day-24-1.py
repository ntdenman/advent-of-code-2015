import sys
sys.setrecursionlimit(2000)

import numpy as np
import copy

in_file_name = "./day-24-input.dat"

# Stole this from Don Knuth 
# "Algorithm F" on p. 361 of vol. 4 of TAoCP
# we represent a possible combination as [c1,c2,c3,...ct] 
# where the ci are indices of masses which are included
# c-vec can be of any length
# The masses are in order s.t. wn > ... > w1 > w0

def visit(com, t, rem, wts, solns): # F2 and F3

    print("Visiting", com, "with t=", t, "and rem=", rem)

    if rem == 0:
        print("-- Solution found:", com[1:])
        solns.append(com[1:])
        return
    # F3
    if com[t] > 0: # last item added is not the lightest item
        if rem >= wts[0]: # can still fit lightest item
            #print("can fit lightest item")
            t += 1 # inc t
            if len(com) <= t:
                com.append(0)
            else:
                com[t] = 0
            rem -= wts[0] # subtract weight from remainder
            #print("Added w0, now:", com, "with t=", t, "and rem=", rem)
            visit(com, t, rem, wts, solns) # return to F2

    # proceed to F4
    try_inc(com, t, rem, wts, solns)

    return

def try_inc(com, t, rem, wts, solns): # F4
    if t == 0:
        print("Terminated at com:", com, "with t=", t, "and rem=", rem)
        return
    else:
        # check for overrun
        if t >= len(com):
            return
        if com[t-1] > (com[t] + 1):
            # if the prev added weight is not immediately the next heaviest
            if rem >= (wts[com[t]+1] - wts[com[t]]): 
                # more remaining than the difference between the prev. added weight
                # and the weight which would be the next heaviest 

                com[t] += 1 # replace the prev added weight with the next heaviest
                rem -= (wts[com[t]] - wts[com[t]-1]) # subtract weight difference from prev
                #print("Now at", com, "with t=", t, "and rem=", rem)
                #print("after swapping weight", wts[com[t]-1], "with", wts[com[t]])
                visit(com, t, rem, wts, solns) # return to F2

    
    test_without(com, t, rem, wts, solns) # proceed to F5

    print("Fell Through step F4")

    return

def test_without(com, t, rem, wts, solns): # F5
    # Now test without the most recently added weight

    if t >= len(com) or t == 0:
        # need to exit the loop once we terminate
        return 

    #print("Testing without prev. weight:", wts[com[t]])
    rem += wts[com[t]]
    t -= 1
    com.pop()

    try_inc(com, t, rem, wts, solns) # return to F4
    return

with open(in_file_name, mode="rt") as infile:

    # get packages 
    pkgs = []
    for line in infile.readlines():
        pkgs.append(int(line))

print(pkgs)

num_groups = 3
group_weight = int(sum(pkgs) // num_groups)

# Find all combinations which meet the target weight of packages
init_solns = []
visit([len(pkgs)], 0, group_weight, pkgs, init_solns) # F1

# Then sort them by the package count 
init_solns.sort(key=len)
#main_solns.sort(key=lambda x:-len(x[0]))

# Far upper bound
min_len = len(pkgs)
min_qe = np.product(pkgs)

# Now to check the initial solutions for balance
for i, soln in enumerate(init_solns):
    pkg_left = copy.copy(pkgs)

    # Move from indices to a list of weights
    sol_wts = []
    for ct in soln:
        sol_wts.append(pkgs[ct])

    # And remove those ised from the remaining list
    for wt in sol_wts:
        pkg_left.remove(wt)

    # For simplicity, reusing the prev. code to find if the remaining packages can be balanced
    second_solns = []
    visit([len(pkg_left)], 0, group_weight, pkg_left, second_solns)

    if len(second_solns) == 0:
        # The remaining packages can't be evenly balanced
        print(sol_wts, np.product(sol_wts), "can't balance")
        continue

    else:
        print(sol_wts, np.product(sol_wts), "balances")
        if len(sol_wts) > min_len:
            print("Longer than shortest option")
            break
        else:
            min_len = len(sol_wts)
            qe = np.product(sol_wts)
            if qe < min_qe:
                min_qe = qe

print("done", min_qe)
