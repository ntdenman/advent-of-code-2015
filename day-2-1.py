import numpy as np 

in_file_name = "./day-2-input.dat"

def parse_dims(dim_string):
    dim_list = dim_string.split('x')
    return dim_list

def calc_area(dim_list):
    l = float(dim_list[0])
    w = float(dim_list[1])
    h = float(dim_list[2])
    sides = [l*w, w*h, l*h]
    base_area = 2*np.sum(sides)
    min_side = np.min(sides)
    return base_area+min_side

total_area = 0

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        total_area += calc_area(parse_dims(line))

print(total_area)
