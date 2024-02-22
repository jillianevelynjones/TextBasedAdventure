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
        self.genders = ["male", "female", "non-binary"]
        self.gender_weights = [50, 45, 5]
        self.skin_colors = ["yellow-brown umber skin", "reddish brown sepia skin", "pale brown ochre skin",
                            "reddish brown russet skin", "brownish orange terra cotta skin", "golden skin",
                            "yellow-brown tawny skin", "gray taupe skin", "khaki colored skin", "light fawn skin",
                            "brown coloring", "ruddy red coloring", "cool grays coloring", "blue coloring",
                            "red skin", "purple skin", "blue skin", "red coloring", "blue coloring",
                            "green coloring", "black coloring", "white coloring", "copper coloring",
                            "brass coloring", "silver coloring", "gold coloring", "bronze coloring",
                            "green skin", "grayish blue skin", "red skin", "black feathers", "brown feathers",
                            "gray feathers", "red feathers", "yellow feathers", "orange feathers", "dark gray skin", "light gray skin", "gray skin",
                            "black fur with white spots", "yellow fur", "orange fur", "yellow fur with orange stripes",
                            "black fur", "white fur", "calico fur", "brown fur", "cinnamon fur", "gray fur",
                            "orange skin with a blue nose", "brown fur", "error - skin color races"]
        self.skin_color_weights = [self.skin_colors.count(color) for color in self.skin_colors]
        self.hair_lengths = ["long", "medium length", "short", "buzzed", "no", " "]
        self.hair_length_weights = [self.hair_lengths.count(length) for length in self.hair_lengths]

    def generate_npcs(self):
        npcs = []
        for i in range(self.num_npcs):
            race = random.choices(self.races, weights=self.race_weights)[0]
            mean_age = 30
            stdev_age = 10
            age = int(random.normalvariate(mean_age, stdev_age))
            gender = random.choices(self.genders, weights=self.gender_weights, k=1)[0]
            skin_color = random.choices(self.skin_colors, weights=self.skin_color_weights, k=1)[0]
            hair_length = random.choices(self.hair_lengths, weights=self.hair_length_weights, k=1)[0]
            
            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling",
                        "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome", "deep gnome",
                        "half elf",
                        "protector aasimar", "scourge aasimar", "fallen aasimar"]:
                self.skin_color = ["yellow-brown umber skin", "reddish brown sepia skin", "pale brown ochre skin",
                                   "reddish brown russet skin", "brownish orange terra cotta skin", "golden skin",
                                   "yellow-brown tawny skin", "gray taupe skin", "khaki colored skin",
                                   "light fawn skin"]
            elif race in ["firbolg", "earth genasi"]:
                self.skin_color = \
                random.choices(["brown coloring", "ruddy red coloring", "cool grays coloring", "blue coloring"],
                               weights=[3, 3, 1, 1])[0]
            elif race in ["infernal tiefling", "feral tiefling"]:
                self.skin_color = random.choices(["red skin", "purple skin", "blue skin"], weights=[4, 4, 2])[0]
            elif race in ["dragonborn", "lizardfolk", "kobold"]:
                self.skin_color = ["red coloring", "blue coloring", "green coloring",
                                   "black coloring", "white coloring", "copper coloring",
                                   "brass coloring", "silver coloring", "gold coloring",
                                   "bronze coloring"]
            elif race in ["half orc", "orc", "goblin"]:
                self.skin_color = ["green skin"]
            elif race in ["goliath", "triton"]:
                self.skin_color = ["grayish blue skin"]
            elif race in ["fire genasi"]:
                self.skin_color = ["red skin"]
            elif race in ["kenku"]:
                self.skin_color = ["black feathers"]
            elif race in ["aarakocra"]:
                if gender in ["female"]:
                    self.skin_color = ["brown feathers", "gray feathers"]
                elif gender in ["male"]:
                    self.skin_color = ["red feathers", "yellow feathers", "orange feathers"]
                else:
                    self.skin_color = ["red feathers", "yellow feathers", "orange feathers",
                                       "brown feathers", "gray feathers"]
            elif race in ["drow", "duergar"]:
                self.skin_color = ["dark gray skin", "light gray skin", "gray skin"]
            elif race in ["tabaxi"]:
                self.skin_color = ["black fur with wfhite spots", "yellow fur", "orange fur",
                                   "yellow fur with orange stripes", "black fur", "white fur",
                                   "calico fur", "brown fur", "cinnamon fur", "gray fur"]
            elif race in ["hobgoblin"]:
                self.skin_color = ["orange skin with a blue nose"]
            elif race in ["bugbear"]:
                self.skin_color = ["brown fur"]
            else:
                self.skin_color = ["error - skin color races"]
            
            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
            "stout halfling", "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome",
            "deep gnome", "half elf", "protector aasimar", "scourge aasimar", "fallen aasimar", "half orc",
            "goliath", "air genasi", "earth genasi", "fire genasi", "water genasi", "duergar dwarf", "drow",
            "hobgoblin", "goblin", "yuan-ti pureblood"]:
                if gender == "female":
                    self.hair_length = ["long", "medium length", "short", "buzzed", "no", " "]
                    self.hair_length_weights = [4, 3, 2, 1, 0, 0]  # Sum equals 6
                elif gender == "male":
                    self.hair_length = ["long", "medium length", "short", "buzzed", "no", " "]
                    self.hair_length_weights = [1, 2, 3, 2, 2, 0]    
                else:
                    self.hair_length = ["long", "medium length", "short", "buzzed", "no", " "]
                    self.hair_length_weights = [3, 3, 3, 1, 0, 0]  # Sum equals 6
            else:
                self.hair_length = ["long", "medium length", "short", "buzzed", "no", " "]
                self.hair_length_weights = [0, 0, 0, 0, 0, 10]  # Ensure one weight is non-zero for the default case


            npc = NewNPC(race, age, gender, skin_color, hair_length)
            npcs.append(npc)
        self.npcs = npcs

        return npcs
    
