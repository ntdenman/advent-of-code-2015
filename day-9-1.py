import numpy as np

in_file_name = "./day-9-input.dat"

def calc_distance(idx_0, idx_1, dist_table):
    if idx_0 > idx_1:
        idx_0, idx_1 = idx_1, idx_0
    return dist_table[idx_0, idx_1]

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_lines = len(lines)
    n_cities = int(np.round(np.sqrt(2*n_lines+1)+0.5))

    dist_grid = np.zeros((n_cities, n_cities), dtype=np.int32)
    
    # I am assuming the input data is always sorted
    # So I can be lazy about indexing 

    dist_vals = []

    for line in lines:
        data = line.split()
        dist_val = np.int32(data[-1])
        dist_vals.append(dist_val)

    idx = np.triu_indices(n_cities, 1)
    dist_grid[idx] = dist_vals

# Then the actual optimization
# Heck, let's just do a random one for fun
n_max = 10000

min_dist = 0

for i in range(n_max):
    path = np.random.permutation(n_cities)
    dist = 0

    for j in range(n_cities-1):
        dist += calc_distance(path[j], path[j+1], dist_grid)

    if i == 0:
        min_dist = dist
    elif dist < min_dist:
            min_dist = dist
            #print(min_dist, path)

print(min_dist)
