import numpy as np

in_file_name = "./day-7-input.dat"

circuit = []

def find_component(com_id):
    for i in range(len(circuit)):
        if circuit[i][0] == com_id:
            return circuit[i]

def get_value(comp_id):
    if(comp_id.isdigit()):
        return np.uint16(comp_id)
    else:
        comp = find_component(comp_id)
        if comp[1] == 'imm':
            return get_value(comp[2])
        elif comp[1] == 'not':
            return np.invert(get_value(comp[2]))
        elif comp[1] == 'AND':
            return np.bitwise_and(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'OR':
            return np.bitwise_or(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'LSHIFT':
            return np.left_shift(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'RSHIFT':
            return np.right_shift(get_value(comp[2]), get_value(comp[3]))
        else:
            raise AssertionError

# loads up the circuit into a legible format
with open(in_file_name, mode="rt") as infile:
    for line in infile:
        tokens = line.split()

        comp_id = tokens[-1]
        op_str = tokens[:-2]

        if len(op_str) == 1:
            # immediate value 
            circuit.append([comp_id, 'imm', op_str[0], 0])
        elif len(op_str) == 2:
            # negation
            circuit.append([comp_id, 'not', op_str[1], 0])
        elif len(op_str) == 3:
            # binary operation
            circuit.append([comp_id, op_str[1], op_str[0], op_str[2]])

print(get_value('a'))
