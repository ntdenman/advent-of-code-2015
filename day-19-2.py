import re

in_file_name = "./day-19-input.dat"

unique_mols = []
counts = []
max_iter = 1000

# Well, this Advent of Code thing sure got me using recursion 
# Also: makes much more sense to work backwards for this one

def explore(in_mol, tar_mol, edits, unique_mols, count, counts):
    count += 1

    # avoid going too far during test runs
    if count > max_iter:
        return

    for edit in edits:
        matches = re.finditer(edit[0], in_mol)

        for m in matches:
            # generate new molecule
            new_mol = in_mol[:m.start()] + edit[1] + in_mol[m.end():]

            if new_mol in unique_mols:
                continue
            else:
                unique_mols.append(new_mol)
            #print(count, ": ", new_mol)

            # done search
            if new_mol == tar_mol:
                print("Match found after", count, "edits")
                counts.append(count)
                return
            else:
                # check new molecule in turn
                explore(new_mol, tar_mol, edits, unique_mols, count, counts)

# Load edits and target from inputs
with open(in_file_name, mode="rt") as infile:
    edit_ops = []

    lines = infile.readlines()

    init_mol = lines[-1].replace("\n","")
    # Always the last line
    # Also need to strip the trailing newline this time

    lines = lines[:-2]
    num_edits = len(lines)
    # removing last two lines, leaving only the edit commands

    for i in range(num_edits):
        line = lines[i].split()
        # reversing in order to work backwards
        edit_ops.append([line[-1], line[0]])

#sorting by length due to greed 
edit_ops.sort(key=lambda x:-len(x[0]))

#print(edit_ops)

explore(init_mol, "e", edit_ops, unique_mols, 0, counts)

print("Fewest Steps:", min(counts))

