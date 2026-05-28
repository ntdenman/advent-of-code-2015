import numpy as np 

in_file_name = "./day-2-input.dat"

def parse_dims(dim_string):
    dim_list = dim_string.split('x')
    return dim_list

def calc_ribbon(dim_list):
    l = float(dim_list[0])
    w = float(dim_list[1])
    h = float(dim_list[2])
    perims = [2*l+2*w, 2*w+2*h, 2*l+2*h]
    min_perim = np.min(perims)
    bow_amt = l*w*h
    return min_perim + bow_amt

total_ribbon = 0

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        total_ribbon += calc_ribbon(parse_dims(line))

print(total_ribbon)
