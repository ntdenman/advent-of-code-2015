import json 

in_file_name = "./day-12-input.json"

def sum_pop(in_obj):
    temp_sum = 0
    if type(in_obj) == dict:
        for key in in_obj.keys():
            temp_sum += sum_pop(in_obj[key])
    elif type(in_obj) == list:
        for val in in_obj:
            temp_sum += sum_pop(val)
    elif type(in_obj) == int:
        return in_obj
    elif type(in_obj) == str:
        return 0
    else:
        print(type(in_obj))
        raise AssertionError
    return temp_sum

with open(in_file_name, mode="rt") as infile:

    json_obj = json.load(infile)

    print(sum_pop(json_obj))

