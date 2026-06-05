import numpy as np

target_val = 36000000
target_val /= 11
# scaling

max_elf = int(target_val)

pres_vals = np.zeros(max_elf, dtype=np.int64)
max_house = 50

# loop over all elves; i is elf number 
for i in range(1,max_elf):
    house_count = 0
    for j in range(i, max_elf, i):
        pres_vals[j] += i
        house_count += 1
        if house_count == max_house:
            break

for i in range(max_elf):
    if pres_vals[i] >= target_val:
        print(i, 11*pres_vals[i])
        break
