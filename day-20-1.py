# second try 
# first attempt, a naive search based on explicit calculation, had absurd runtime 

import numpy as np

target_val = 36000000
target_val /= 10
# scaling

# New idea: explicitly calculate out the presents in a single large loop
max_elf = int(target_val)

pres_vals = np.zeros(max_elf, dtype=np.int64)

# loop over all elves; i is elf number 
for i in range(1,max_elf):
    for j in range(i, max_elf, i):
        pres_vals[j] += i

for i in range(max_elf):
    if pres_vals[i] >= target_val:
        print(i, 10*pres_vals[i])
        break
