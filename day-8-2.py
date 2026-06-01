import numpy as np

in_file_name = "./day-8-input.dat"

old_code_chars = 0
new_code_chars = 0

with open(in_file_name, mode="rt") as infile:
    for line in infile:
        line_bytes = bytes(line, 'ascii')
        print(line)
        
        #strip last byte for newline
        line_bytes = line_bytes[:-1]

        # strip outer quotation marks 
        line_bytes = line_bytes[1:-1]
        old_code_chars += 2

        old_code_chars += len(line_bytes)

        # each line will have two enclosing quotation marks
        # and then escape the previous quotes
        # for a total of six
        new_code_chars += 6

        line_text = line_bytes.decode(encoding='ascii')
        print("begin: ", line_text)

        for i in range(len(line_text)):
            if(line_text[i] == "\\"):
                new_code_chars += 1
            elif(line_text[i] == "\""):
                new_code_chars += 1
            new_code_chars += 1

print(old_code_chars, new_code_chars, new_code_chars - old_code_chars)
