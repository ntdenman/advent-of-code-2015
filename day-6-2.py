import numpy as np

in_file_name = "./day-6-input.dat"

lights = np.zeros((1000,1000), dtype=np.int32)

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        offset = 0
        tokens = line.split()

        if len(tokens) == 4:
            cmd = 'xor'
            offset = 0
        elif tokens[1] == 'on':
            cmd = 'on'
            offset = 1
        elif tokens[1] == 'off':
            cmd = 'off'
            offset = 1
        else:
            raise AssertionError 

        [x0, y0] = np.asarray(tokens[1+offset].split(","), dtype=np.int32)
        [x1, y1] = np.asarray(tokens[3+offset].split(","), dtype=np.int32)
        x1 += 1
        y1 += 1
    
        if cmd == 'on':
            lights[x0:x1,y0:y1] += 1
        elif cmd == 'off':
            lights[x0:x1,y0:y1] = np.maximum(lights[x0:x1,y0:y1]-1, 0)
        elif cmd == 'xor':
            lights[x0:x1,y0:y1] += 2
        else:
            raise AssertionError

print(np.sum(lights))
