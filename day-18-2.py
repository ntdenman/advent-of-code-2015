import numpy as np

# Conway's Game of Life
# but make it Festive

in_file_name = "./day-18-input.dat"

n_iter = 100

def get_val(grid, x, y):
    if (x < 0) or (y < 0) or (x >= len(grid)) or (y >= len(grid)):
        return 0
    else:
        return grid[x,y]

def get_update(grid, x, y):
    if ((x == 0) and (y == 0)) or \
            ((x == 0) and (y == len(grid)-1)) or \
            ((x == len(grid)-1) and (y == 0)) or \
            ((x == len(grid)-1) and (y == len(grid)-1)):
        return 1 # corners stuck on
    adj_sum = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            else:
                adj_sum += get_val(grid, x+i, y+j)
    if grid[x,y] == 0: #was off
        if adj_sum == 3:
            return 1
        else:
            return 0
    else:
        if (adj_sum == 2) or (adj_sum == 3):
            return 1
        else:
            return 0

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_lines = len(lines)

    grid_dim = n_lines
    old_grid = np.zeros((grid_dim, grid_dim), dtype=np.int8)

    for i in range(n_lines):
        for j in range(len(lines[i])):
            if ((i == 0) and (j == 0)) or \
                   ((i == 0) and (j == n_lines-1)) or \
                   ((i == n_lines-1) and (j == 0)) or \
                   ((i == n_lines-1) and (j == n_lines-1)):
                old_grid[i,j] = 1
            elif lines[i][j] == "#":
                old_grid[i,j] = 1
            # otherwise leave as 0

for t in range(n_iter):
    new_grid = np.zeros_like(old_grid)
    for i in range(grid_dim):
        for j in range(grid_dim):
            new_grid[i,j] = get_update(old_grid, i, j)
    old_grid = new_grid

print(np.sum(new_grid))
