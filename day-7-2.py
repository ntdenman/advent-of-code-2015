import numpy as np

in_file_name = "./day-7-input.dat"

circuit = []
cache = []

def find_component(comp_id):
    for i in range(len(cache)):
        if cache[i][0] == comp_id:
            return [comp_id, 'imm', cache[i][1], 0]
    for i in range(len(circuit)):
        if circuit[i][0] == comp_id:
            return circuit[i]

def get_value(comp_id):
    if isinstance(comp_id, np.uint16):
        return comp_id
    elif(comp_id.isdigit()):
        return np.uint16(comp_id)
    else:
        if(comp_id == 'b'):
            return np.uint16(956)
        comp = find_component(comp_id)
        if comp[1] == 'imm':
            return get_value(comp[2])
        elif comp[1] == 'not':
            ret_val = np.invert(get_value(comp[2]))
        elif comp[1] == 'AND':
            ret_val = np.bitwise_and(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'OR':
            ret_val = np.bitwise_or(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'LSHIFT':
            ret_val = np.left_shift(get_value(comp[2]), get_value(comp[3]))
        elif comp[1] == 'RSHIFT':
            ret_val = np.right_shift(get_value(comp[2]), get_value(comp[3]))
        else:
            raise AssertionError
        cache.append([comp_id, ret_val])
        return ret_val

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
