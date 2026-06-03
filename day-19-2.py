import re

in_file_name = "./day-19-input.dat"

edit_ops = []
max_iter = 10

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()

    target_mol = lines[-1].replace("\n","")
    # Always the last line
    # Also need to strip the trailing newline this time

    lines = lines[:-2]
    num_edits = len(lines)
    # removing last two lines, leaving only the edit commands

    for i in range(num_edits):
        line = lines[i].split()
        edit_ops.append([line[0], line[-1]])

# Naive breadth-first search
# Made use of the fact that in my list of substitutions
# none made the molecule shorter
# so we can prune branches which go over the target length

# Initial condition
prev_mols = ["e"]

for i in range(max_iter):

    unique_mols = []
    # Q: does resetting this save us time
    # considering that it means we keep running loops?

    # loop over all previous molecules
    while(len(prev_mols) > 0):
        start_mol = prev_mols.pop()

        # all possible edits for this molecule
        for edit in edit_ops:

            # find candidate substitutions
            matches = re.finditer(edit[0], start_mol)

            for m in matches:
                # do replacement
                new_mol = start_mol[:m.start()] + edit[1] + start_mol[m.end():]

                if len(new_mol) > len(target_mol):
                    continue
                # check if new_mol already seen
                if not new_mol in unique_mols:
                    unique_mols.append(new_mol)

    if target_mol in unique_mols:
        print("Match Found in", i+1, "steps")
        break
    else:
        print("No match at step", i+1, "from", len(unique_mols), "options")
        prev_mols = unique_mols
