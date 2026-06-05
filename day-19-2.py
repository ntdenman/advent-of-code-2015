import re

in_file_name = "./day-19-input.dat"

# The previous version having proved unsuitable,
# I did look up some discussions

# It turns out there is a significant pattern in the input
# which makes an algebraic solution possible:
# all replacements are either one element to two elements
# (so they lengthen the molecule by 1)
# or to []Rn[...]Ar
# where the inner portion is an alternating sequence of some length with * and Y

# Load only target
with open(in_file_name, mode="rt") as infile:

    lines = infile.readlines()
    init_mol = lines[-1].replace("\n","")

# Use the regularity:

print(init_mol)
print(re.findall("[A-Z]", init_mol))
num_elem = len(re.findall("[A-Z]", init_mol))
num_RnAr = len(re.findall("Rn|Ar", init_mol))
num_Y = len(re.findall("Y", init_mol))

min_steps = num_elem - (num_RnAr + 2*num_Y + 1)
print(min_steps)
