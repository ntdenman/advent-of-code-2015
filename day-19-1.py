import re

in_file_name = "./day-19-input.dat"

edit_ops = []
unique_mols = []

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()

    start_mol = lines[-1]
    # Always the last line

    lines = lines[:-2]
    num_edits = len(lines)
    # removing last two lines, leaving only the edit commands

    for i in range(num_edits):
        line = lines[i].split()
        edit_ops.append([line[0], line[-1]])

    for edit in edit_ops:
        # find candidates
        matches = re.finditer(edit[0], start_mol)
        for m in matches:
            # do replacement
            new_mol = start_mol[:m.start()] + edit[1] + start_mol[m.end():]
            # check if new_mol already seen
            if not new_mol in unique_mols:
                unique_mols.append(new_mol)

print(len(unique_mols))
