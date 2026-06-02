import numpy as np

in_file_name = "./day-16-input.dat"

known_info = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

falsified = True

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_aunts = len(lines)

    for i in range(n_aunts):
        falsified = False

        line = lines[i].replace(',', '').replace(':','').split()
        line = line[2:]
        n_facts = int(len(line)/2)

        for j in range(n_facts):
            if (line[2*j] == "goldfish") or (line[2*j] == "pomeranians"):
                if int(line[2*j+1]) >= int(known_info[line[2*j]]):
                    falsified = True
                    break
            elif (line[2*j] == "cats") or (line[2*j] == "trees"):
                if int(line[2*j+1]) <= int(known_info[line[2*j]]):
                    falsified = True
                    break
            elif int(known_info[line[2*j]]) != int(line[2*j+1]):
                falsified = True
                break
        if falsified:
            continue
        else:
            print("Match Found at Sue ", i+1)
