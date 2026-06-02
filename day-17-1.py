import numpy as np

in_file_name = "./day-17-input.dat"

target_liters = 150

volumes = []

def explore(vols, index, rem_vol):
    ret_val = 0
    if rem_vol == 0:# last step hit the target
        return 1
    elif index == len(vols):# hit end of vector w/o 0 vol. left
        return 0
    elif vols[index] > rem_vol: #can't fill this vol
        ret_val += explore(vols, index+1, rem_vol) # only not included path
        return ret_val
    else:
        ret_val += explore(vols, index+1, rem_vol) # not included path
        ret_val += explore(vols, index+1, rem_vol - vols[index]) # included path
        return ret_val

with open(in_file_name, mode="rt") as infile:
    for line in infile.readlines():
        volumes.append(np.int32(line))
    volumes.sort(reverse=True)
    print(volumes)

#volumes = [20, 15, 10, 5, 5]
#target_liters = 25

print(explore(volumes, 0, target_liters))
