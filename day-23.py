import numpy as np

in_file_name = "./day-23-input.dat"

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()

    instr = []

    for i in range(len(lines)):
        instr.append(lines[i].replace(",","").split())

# edit for part two
reg = {"a":1, "b":0}

instr_pointer = 0
print(instr)

while(True):

    if instr_pointer >= len(instr) or instr_pointer < 0:
        print(instr_pointer)
        break

    # load components of instruction
    op = instr[instr_pointer][0]
    r = instr[instr_pointer][1]
    if len(instr[instr_pointer]) == 3:
        of = instr[instr_pointer][2]

    # lazy debug
    print(instr_pointer, instr[instr_pointer], "|", reg)

    if op == "hlf":
        reg[r] = reg[r] / 2

    elif op == "tpl":
        reg[r] = reg[r] * 3

    elif op == "inc":
        reg[r] = reg[r] + 1

    elif op == "jmp":
        instr_pointer += int(r)
        continue

    elif op == "jio":
        if reg[r] == 1:
            instr_pointer += int(of)
            continue

    elif op == "jie":
        if (reg[r] % 2) == 0 :
            instr_pointer += int(of)
            continue
    else:
        raise AssertionError

    print("next")
    instr_pointer += 1

print(reg)
