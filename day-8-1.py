import numpy as np

in_file_name = "./day-8-input.dat"

code_chars = 0
string_vals = 0

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        line_bytes = bytes(line, 'ascii')
        print((line), "length: ", len(line_bytes)-3)
        
        #strip last byte for newline
        line_bytes = line_bytes[:-1]

        # strip outer quotation marks 
        line_bytes = line_bytes[1:-1]
        code_chars += 2

        if len(line_bytes) == 0:
            continue
 
        code_chars += len(line_bytes)

        line_text = line_bytes.decode(encoding='ascii')
        print("begin: ", line_text)

        if len(line_bytes) >= 2:
            i = 0
            while(i < len(line_bytes)): # not 'for' due to lenth changing during loop
                if(line_bytes[i] == 0x5c): # backslash detected
                    if(line_bytes[i+1] == 0x5c) or (line_bytes[i+1] == 0x22): # \\ or \"
                        print("found:", line_bytes[i:i+2].decode())
                        line_bytes = line_bytes[0:i] + line_bytes[i+2:]
                        string_vals += 1
                        i = 0
                        continue
                i += 1

        line_text = line_bytes.decode(encoding='ascii')
        print(line_text)

        # check for escaped hex literals 
        # any remaining backslashes are non-escaped by construction
        if len(line_bytes) >= 4:
            i = 0
            while(i < len(line_bytes)): # not 'for' due to lenth changing during loop
                if line_text[i:i+2] == "\\x":
                    if line_bytes[i+2:i+4].isascii():
                        print("found:", line_bytes[i:i+4].decode())
                        line_bytes = line_bytes[0:i] + line_bytes[i+4:]
                        line_text = line_bytes.decode(encoding='ascii')
                        string_vals += 1 
                        i = 0
                i += 1

        line_text = line_bytes.decode(encoding='ascii')
        print(line_text)

        string_vals += len(line_bytes)

        print(len(line_bytes), "\n")

print(code_chars, string_vals, code_chars - string_vals)
