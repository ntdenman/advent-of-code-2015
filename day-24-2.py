import numpy as np
import copy

in_file_name = "./day-24-input.dat"

# Stole this from Don Knuth 
# "Algorithm F" on p. 361 of vol. 4A of TAoCP
# we represent a possible combination as [c1,c2,c3,...ct] 
# where the ci are indices of masses which are included
# c-vec can be of any length
# The masses are in order s.t. wn > ... > w1 > w0

# Re-written from prev version in the form of nested loops
# which will avoid the Giant Recursive Stack of Doom

def knap_loop(total, wts, solns):

    # F1 initialization
    t = 0
    cvec = [len(wts)]
    rem = copy.copy(total)

    skip_F3 = False

    while(True):
        # F2
        if rem == 0:
            #print("-- Solution found:", cvec[1:])
            solns.append(cvec[1:])

        #F3
        if not skip_F3:
            if cvec[t] > 0: # last item added is not the lightest item
                if rem >= wts[0]: # can still fit lightest item
                    #print("can fit lightest item")
                    t += 1 # inc t
                    if len(cvec) <= t:
                        cvec.append(0)
                    else:
                        cvec[t] = 0
                    rem -= wts[0] # subtract weight from remainder
                    continue # return to F2

        # F4 
        if t == 0:
            #print("Terminated at com:", com, "with t=", t, "and rem=", rem)
            break
        else:
            # check for overrun
            if t >= len(cvec):
                print("overrun")
                continue
             # or break?
            if cvec[t-1] > (cvec[t] + 1):
                # if the prev added weight is not immediately the next heaviest
                if rem >= (wts[cvec[t]+1] - wts[cvec[t]]): 
                    # more remaining than the difference between the prev. added weight
                    # and the weight which would be the next heaviest 

                    cvec[t] += 1 # replace the prev added weight with the next heaviest
                    rem -= (wts[cvec[t]] - wts[cvec[t]-1]) # subtract weight difference from prev
                    #print("Now at", com, "with t=", t, "and rem=", rem)
                    #print("after swapping weight", wts[com[t]-1], "with", wts[com[t]])
                    skip_F3 = False
                    continue # return to F2


        # F5
        # Try without most recent weight
        rem += wts[cvec[t]]
        t -= 1
        cvec.pop()
        
        # return to F4
        skip_F3 = True
        continue


with open(in_file_name, mode="rt") as infile:

    # get packages 
    pkgs = []
    for line in infile.readlines():
        pkgs.append(int(line))

print(pkgs)

num_groups = 4
group_weight = int(sum(pkgs) // num_groups)

# Find all combinations which meet the target weight of packages
init_solns = []
knap_loop(group_weight, pkgs, init_solns)

# Then sort them by the package count 
init_solns.sort(key=len)
#main_solns.sort(key=lambda x:-len(x[0]))

# Far upper bound
min_len = len(pkgs)
min_qe = np.prod(pkgs, dtype=np.float64) #int64 too small

# Now to check the initial solutions for balance
# Note: now have to check that there exist _two_ additional balanced groups
for soln in init_solns:
    if len(soln) > min_len:
        print("Longer than shortest option")
        break # solns are in order

    # Move from indices to a list of weights
    sol_wts = []
    for ct in soln:
        sol_wts.append(pkgs[ct])

    # break early to save time
    qe = np.prod(sol_wts, dtype=np.float64)
    if qe >= min_qe:
        #print("QE not lower than current min", qe, min_qe)
        continue

    # And remove those used from the remaining list
    pkg_left = copy.copy(pkgs)
    for wt in sol_wts:
        pkg_left.remove(wt)

    second_solns = []
    knap_loop(group_weight, pkg_left, second_solns)

    if len(second_solns) == 0:
        # The remaining packages can't be evenly balanced
        print(sol_wts, np.product(sol_wts), "can't balance")
        continue

    else:
        # now know that there's at least one balancing group
        # but for four total, we need to find an additional one
        # using only the remaining packages
        # it's basically the above but we only care if a sol'n exists
        can_rebalance = False
        for soln_2 in second_solns:
            sol_wts_2 = []
            for ct2 in soln_2:
                sol_wts_2.append(pkg_left[ct2])
            pkg_left_2 = copy.copy(pkg_left)
            for wt2 in sol_wts_2:
                pkg_left_2.remove(wt2)
            third_solns = []
            knap_loop(group_weight, pkg_left_2, third_solns)
            if len(third_solns) == 0:
                continue
            else:
                # a solution exists
                can_rebalance = True
                break
        if not can_rebalance:
            print(sol_wts, np.product(sol_wts), "can't rebalance")
            continue
        else:
            print(sol_wts, np.product(sol_wts), "balances")
            min_len = len(sol_wts)
            if qe < min_qe:
                min_qe = qe
                print("new low:", min_qe)

print("done, lowest QE is:", min_qe)
