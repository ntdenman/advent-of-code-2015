import numpy as np 

in_file_name = "./day-3-input.dat"

moves = {'^':1.j, 
         '>':1, 
         'v':-1.j, 
         '<':-1 } 

visited = np.zeros(1, dtype=np.complex64)
cur_locn = visited[0]

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        for i in range(len(line)):
            if line[i] == '\n':
                break
            else:
                cur_locn += moves[line[i]]
                if cur_locn not in visited:
                    visited = np.append(visited, [cur_locn], 0)

print(len(visited))
