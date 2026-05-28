import re 

# Given this is all regexes, I'm sure there's a pleasant way to do this with grep

in_file_name = "./day-5-input.dat"

nice_count = 0

def is_nice(line_in):
    vowel_count = len(re.findall("[aeiou]", line_in))
    double_count = len(re.findall("(.)\\1", line_in)) # backslashes again
    bad_count = len(re.findall("ab|cd|pq|xy", line_in))

    return ( (vowel_count >= 3) 
            and (double_count >= 1) 
            and not (bad_count > 0))

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        if is_nice(line):
            nice_count += 1

print(nice_count)
