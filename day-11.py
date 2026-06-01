import re 

#prev_pw = "hepxcrrq"
prev_pw = "hepxxyzz"
#prev_pw = "ghijklmn"

def inc_char(in_char):
    if in_char == "z":
        return True, "a"
    else:
        next_char = chr(ord(in_char)+1)
        return False, next_char

def inc_string(in_str):
    carry, new_char = inc_char(in_str[-1])

    if len(in_str) == 1:
        return new_char
    elif carry:
        ret_str = inc_string(in_str[:-1]) + new_char
        return ret_str
    else:
        ret_str = in_str[:-1] + new_char
        return ret_str

def check_string(in_str):
    bad_count = len(re.findall("[ilo]", in_str))
    if bad_count > 0:
        return False
    double_count = len(re.findall("(.)\\1", in_str))
    if double_count < 2:
        return False
    for i in range(len(in_str)-2):
        start = in_str[i]
        if (in_str[i+1] == chr(ord(start)+1)) and ((in_str[i+2] == chr(ord(start)+2))):
            return True
    return False

while True:
    new_pw = inc_string(prev_pw)
    if check_string(new_pw):
        break
    else:
        prev_pw = new_pw

print(new_pw)
