import numpy as np

# function which returns the successor coord
# to a given x,y pair
def next_coords(vec):
    x, y = vec
    if y > 1:
        # usual step
        return [x+1, y-1]
    else:
        # hit the top
        return [1, x+y]

# next code in sequence
def next_code(in_code):
    return (in_code*252533) % 33554393

coords = [1,1]
code = np.int64(20151125)
target_coords = [3019,3010] # note x is column and y is row
#target_coords = [3,3]

while(True):
    coords = next_coords(coords)
    code = next_code(code)

    if coords == target_coords:
        break

print(coords, code)

