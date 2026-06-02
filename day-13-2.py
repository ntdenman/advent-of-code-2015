import numpy as np

in_file_name = "./day-13-input.dat"

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_lines = len(lines)
    n_ppl = int(np.round(np.sqrt(n_lines+.25)+0.5))

    # Leaving room for myself
    hap_grid = np.zeros((n_ppl+1, n_ppl+1), dtype=np.int32)
    
    # Again relying on sorted/structured input 
    # otherwise would need string compare / lookup
    k = 0
    for i in range(n_ppl):
        for j in range(n_ppl):
            if i == j:
                continue
            else:
                line = lines[k]
                data = line.split()
                if data[2] == "gain":
                    hap_val = np.int32(data[3])
                elif data[2] == "lose":
                    hap_val = -1*np.int32(data[3])
                hap_grid[i,j] = hap_val
                k += 1

# As before, going to just use random sampling
n_max = 10000

max_hap = 0

for i in range(n_max):
    seating = np.random.permutation(n_ppl+1)
    # random seating arrangement 

    hap = 0

    for j in range(n_ppl+1):
        hap += hap_grid[seating[j],seating[j-1]]
        hap += hap_grid[seating[j-1],seating[j]]
        # Exploiting negative indexing for circular adjacency

    if (hap > max_hap) or (i == 0): # Lazy evaluation wins again
        max_hap = hap
        print(seating, hap)

print(max_hap)
