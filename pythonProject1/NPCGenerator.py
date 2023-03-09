import random
from NPC import NPC

"""Next, we'll create a class called NPCGenerator 
that will generate a list of random NPCs based on the user input"""


class NPCGenerator:
    def __init__(self, num_npcs):
        self.num_npcs = num_npcs

    def generate_npcs(self):
        races = ["human", "wood elf", "mountain dwarf", "lightfoot halfling",
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
        race_weights = [1500, 350, 350, 350,
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
        genders = ["male", "female", "non-binary"]
        gender_weights = [50, 45, 5]

        def correct_npcs(race, gender):

            if race in ["human", "high elf", "wood elf",
                        "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling",
                        "forest gnome", "rock gnome", "deep gnome",
                        "half elf", "protector aasimar", "scourge aasimar", "fallen aasimar"]:
                cskin_color = random.choices(["yellow-brown umber skin", "reddish brown sepia skin",
                                              "pale brown ochre skin", "reddish brown russet skin",
                                              "brownish orange terra cotta skin", "golden skin",
                                              "yellow-brown tawny skin", "gray taupe skin", "khaki colored skin",
                                              "light fawn skin"])
            elif race in ["firbolg", "earth genasi"]:
                cskin_color = random.choices(["brown coloring", "ruddy red coloring", "cool grays coloring",
                                              "blue coloring"])
            elif race in ["infernal tiefling", "feral tiefling"]:
                cskin_color = random.choices(["red skin", "purple skin", "blue skin"])
            elif race in ["dragonborn", "lizardfolk", "kobold"]:
                cskin_color = random.choice(["red coloring", "blue coloring", "green coloring",
                                             "black coloring", "white coloring", "copper coloring",
                                             "brass coloring", "silver coloring", "gold coloring",
                                             "bronze coloring"])
            elif race in ["half orc", "orc", "goblin"]:
                cskin_color = ["green skin"]
            elif race in ["goliath", "triton"]:
                cskin_color = ["grayish blue skin"]
            elif race in ["fire genasi"]:
                cskin_color = ["red skin"]
            elif race in ["kenku"]:
                cskin_color = ["black feathers"]
            elif race in ["aarakocra"]:
                if gender in ["female"]:
                    cskin_color = random.choice(["brown feathers", "gray feathers"])
                elif gender in ["male"]:
                    cskin_color = random.choice(["red feathers", "yellow feathers", "orange feathers"])
                else:
                    cskin_color = random.choice(["red feathers", "yellow feathers", "orange feathers",
                                                 "brown feathers", "gray feathers"])
            elif race in ["drow", "duergar"]:
                cskin_color = random.choice(["dark gray skin", "light gray skin", "gray skin"])
            elif race in ["tabaxi"]:
                cskin_color = random.choice(["black fur with white spots", "yellow fur", "orange fur",
                                             "yellow fur with orange stripes", "black fur", "white fur",
                                             "calico fur", "brown fur", "cinnamon fur", "gray fur"])
            elif race in ["hobgoblin"]:
                cskin_color = ["orange skin with a blue nose"]
            elif race in ["bugbear"]:
                cskin_color = ["brown fur"]
            else:
                cskin_color = ["error - skin color races"]

            return cskin_color

        npcs = []
        for i in range(self.num_npcs):
            race = random.choices(races, weights=race_weights)[0]
            print(race)
            age = random.randint(15, 90)
            print(age)
            gender = random.choices(genders, weights=gender_weights)[0]
            print(gender)
            skin_color = correct_npcs(race, gender)
            print(skin_color)

            npc = NPC(race, age, gender, skin_color)
            npcs.append(npc)
        return npcs
