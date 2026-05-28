import re 

# Given this is all regexes, I'm sure there's a pleasant way to do this with grep

in_file_name = "./day-5-input.dat"

nice_count = 0

def is_nice(line_in):
    dubdub_count = len(re.findall("(..).*\\1", line_in))
    trio_count = len(re.findall("(.).\\1", line_in))

    return (dubdub_count > 0 ) and ( trio_count > 0)

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        if is_nice(line):
            nice_count += 1

print(nice_count)
