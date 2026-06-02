import numpy as np

in_file_name = "./day-15-input.dat"

n_properties = 5
total_tsp = 100
total_cal = 500

# This got a bit out of hand
# At this specific of a constraint,
# the brute-force method ended up being way faster than the alternatives

def check_recipe(recipe, food_props):
    # total of 100 tsp, all positive values
    # and now: total calories must be 500
    old_check = (sum(recipe) == total_tsp) and (min(recipe) >= 0)
    if not old_check:
        return False
    else:
        cal = 0
        for i in range(len(recipe)):
            cal += recipe[i]*food_props[-1, i]
        return (int(cal) == total_cal)
    
def get_score(recipe, food_props):
    score = 1
    for i in range(n_properties-1): # calories are a constraint
        prop_score = 0
        for j in range(len(recipe)):
            prop_score += recipe[j]*food_props[i,j]
        if prop_score <= 0:
            return 0
        else:
            score *= prop_score
    return score

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_food = len(lines)

    food_data = np.zeros((n_properties, n_food))
    for i in range(n_food):
        line = lines[i].replace(',', '').split()
        for j in range(n_properties):
            food_data[j,i] = np.int32(line[2*(j+1)])

prev_recipe = np.zeros(n_food)
prev_score = 0

for i in range(total_tsp):
    for j in range(total_tsp - i):
        for k in range(total_tsp - (i+j)):

            l = total_tsp - (i+j+k)
            new_recipe = [i,j,k,l]

            if check_recipe(new_recipe, food_data):
                new_score = get_score(new_recipe, food_data)

                if new_score > prev_score:
                    prev_recipe = new_recipe
                    prev_score = new_score

print(prev_recipe, prev_score)
