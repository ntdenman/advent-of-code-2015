import numpy as np

in_file_name = "./day-15-input.dat"

n_properties = 5
total_tsp = 100

def check_recipe(recipe):
    # total of 100 tsp, all positive values
    return (sum(recipe) == total_tsp) and (min(recipe) >= 0)
    
def get_score(recipe, food_props):
    score = 1
    for i in range(n_properties-1): # ignoring calories for now 
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

# Unlike the previous optimization problems,
# this is much more continuous-ish
# so I'll be moving to simulated annealing

prev_recipe = np.zeros(n_food, dtype = np.int32)
prev_recipe[0] += 100
prev_score = get_score(prev_recipe, food_data)

# simulated annealing constants
temp = 1E7
temp_scaling = .9

# size of changes to recipe
step = 10

max_iter = 10000

for i in range(max_iter):
    recipe_delta = np.random.randint(low=-1*step, high=step, size=n_food)
    recipe_delta[-1] = -1*np.sum(recipe_delta[:-1])
    new_recipe = prev_recipe + recipe_delta
    
    if not check_recipe(new_recipe): # fails conditions
        continue
    
    new_score = get_score(new_recipe, food_data)

    if new_score > prev_score: # always accept positive move
        prev_recipe = new_recipe
        prev_score = new_score
    else:
        transition_prob = np.exp((new_score - prev_score) / temp)

        if np.random.random() < transition_prob: # accept transition
            prev_recipe = new_recipe
            prev_score = new_score

    temp *= temp_scaling

print(prev_recipe, prev_score)
