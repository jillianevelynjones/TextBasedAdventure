import random
from NewNPC import NewNPC

class NewNPCGenerator:
    def __init__(self, num_npcs):
        self.num_npcs = num_npcs
        self.races = ["human", "wood elf", "mountain dwarf", "lightfoot halfling",
                      "forest gnome", "stout halfling", "rock gnome",
                      "dragonborn", "hill dwarf", "high elf",
                      "half elf", "aarakocra", "half orc",
                      "infernal tiefling", "protector aasimar", "tabaxi",
                      "firbolg", "triton", "kenku",
                      "scourge aasimar", "fallen aasimar", "goliath",
                      "water genasi", "air genasi", "earth genasi",
                      "fire genasi", "feral tiefling", "eladrin elf",
                      "ghostwise halfling", "deep gnome", "lizardfolk",
                      "duergar dwarf", "drow", "kobold", "orc",
                      "hobgoblin", "goblin", "bugbear", "yaun-ti pureblood"]
        self.race_weights = [1500, 350, 350, 350,
                             350, 300, 300,
                             250, 250, 250,
                             250, 200, 200,
                             100, 100, 90,
                             80, 75, 70,
                             65, 60, 55,
                             50, 50, 50,
                             50, 40, 35,
                             30, 30, 25,
                             10, 10, 5,
                             5, 3, 3,
                             2, 1]
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
    
