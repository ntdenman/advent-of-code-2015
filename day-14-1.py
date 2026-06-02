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
        print(self.name, status, "at position", self.position, " with energy:", self.energy)


with open(in_file_name, mode="rt") as infile:
    lines = infile.readlines()
    n_deer = len(lines)

    deer_vector = []

    for i in range(n_deer):
        deer_data = lines[i].split()
        deer_vector.append(deer(deer_data[0], deer_data[3], deer_data[6], deer_data[13]))

time_max = 2505

for t in range(time_max):
    for dr in deer_vector:
        if t > (time_max - 10):
            print("Time ", t)
            dr.report()
        dr.update()
