import hashlib
import numpy as np 

secret_key = "ckczppom"
#secret_key = "abcdef"
#secret_key = "pqrstuv"

fmt_string = secret_key + "{0:d}"

i = np.uint64(0)

while(True):
    i += np.uint64(1)

    test_string = fmt_string.format(i)

    hash_result = hashlib.md5(test_string.encode()).hexdigest()
    
    #if(hash_result[0:5] == "00000"): # Part One
    if(hash_result[0:6] == "000000"): # Part Two
        break

print(i)
