import random
from NewNPC import NewNPC

class NewNPCGenerator:
    def __init__(self, num_npcs):
        self.num_npcs = num_npcs
        self.races = ["human", "elf", "dwarf"]
        self.genders = ["male", "female"]

    def generate_npcs(self):
        npcs = []
        for i in range(self.num_npcs):
            race = random.choice(self.races)
            mean_age = 30
            stdev_age = 10
            age = int(random.normalvariate(mean_age, stdev_age))
            gender = random.choice(self.genders)
            
            npc = NewNPC(race, age, gender)
            npcs.append(npc)
        self.npcs = npcs

        return npcs
    
