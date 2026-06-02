import numpy as np

# Going to go object-oriented on this one 
# For the sake of actually using Python as Python

in_file_name = "./day-14-input.dat"

class deer:
    def __init__(self, name, speed, endurance, rest_time):
        self.name = name
        self.speed = np.int32(speed)
        self.endurance = np.int32(endurance)
        self.rest_time = -1*np.int32(rest_time)

        # Start at position 0, flying with full energy
        self.position = 0
        self.aloft = True
        self.energy = self.endurance

        # Now with scores
        self.score = 0

    def update(self):
        if self.aloft: #flying 
            self.position += self.speed
            self.energy -= 1 

            if self.energy == 0: # time to rest
                self.aloft = False
                self.energy = self.rest_time

        else: # resting
            self.energy +=1
            if self.energy == 0: # done resting 
                self.aloft = True
                self.energy = self.endurance

    def report(self):
        if self.aloft:
            status = "Flying"
        else:
            status = "Resting"
        print(self.name, status, "at position", self.position, " with energy", self.energy, "and score", self.score)

    def get_position(self):
        return self.position

    def inc_score(self):
        self.score += 1

with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_deer = len(lines)

    deer_vector = []

    for i in range(n_deer):
        deer_data = lines[i].split()
        deer_vector.append(deer(deer_data[0], deer_data[3], deer_data[6], deer_data[13]))

time_max = 2505

for t in range(time_max):
    max_dist = 0
    max_deer = 0
    dists = []

    for dr in deer_vector:
        dr.update()
        dists.append(dr.get_position())

    max_dist = max(dists)

    for i in range(n_deer):
        dr = deer_vector[i]
        dist = dr.get_position()
        if dist == max_dist:
            deer_vector[i].inc_score()
        #dr.report()

    if t > (time_max - 10):
        print("After Second: ", t+1)
        for dr in deer_vector:
            dr.report()

