import random
from NewNPC import NewNPC
from NewNPCName import NewNPCName

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
        self.skin_color_weights = [self.skin_colors.count(skincolor) for skincolor in self.skin_colors]
        self.hair_lengths = ["long", "medium length", "short", "buzzed", "no", " "]
        self.hair_length_weights = [self.hair_lengths.count(length) for length in self.hair_lengths]
        self.hair_textures = ["straight", "wavy", "curly", "kinky curly", " "]
        self.hair_texture_weights = [self.hair_textures.count(texture) for texture in self.hair_textures]
        self.hair_colors = ["brown", "black", "blonde", "ginger", "red", "orange", "green", "blue", "purple", " "]
        self.hair_color_weights = [self.hair_colors.count(haircolor) for haircolor in self.hair_colors]
        self.facial_hairs = [" ", "stubble", "short beard", "long beard", "mustache", "mutton chops"]
        self.facial_hair_weights = [self.facial_hairs.count(facial) for facial in self.facial_hairs]
        self.physical_features1 = ["completely normal", "with", "fat", "skinny", "short", "tall", "built", "wearing glasses", "missing", "scarred"]
        self.physical_features2 = [" ", "butterfly tattoo", "rose tattoo",
                                   "dragon tattoo", "flower tattoo", "snake tattoo",
                                   "geometric tattoo", "lion tattoo", "heart tattoo",
                                   "skull tattoo", "tribal tattoo", "nautical tattoo",
                                   "moon tattoo", "pierced ear", "pierced cartilage",
                                   "pierced nose", "eyebrow piercing", "lip piercing",
                                   "an ear", "an arm", "a hand",
                                   "a finger", "both arms", "a leg",
                                   "both legs", "above the eye", "across the nose",
                                   "on the cheek", "on the shoulder", "on their arm",
                                   "on their hand", "on their back", "on their leg",
                                   "error - physical feature 2"]
        self.physical_feature2_weights = [self.physical_features2.count(feature) for feature in self.physical_features2]
        self.speech_patterns1 = ["in a normal tone", "in a soft spoken voice", "loudly",
                                 "quickly", "slowly", "with a heavy",
                                 "in a mumble", "in a stutter", "with foul language"]
        self.speech_patterns2 = [" ", "midwestern accent", "english accent", "scottish accent",
                                 "russian accent", "french accent", "southern accent",
                                 "californian accent"]
        self.speech_pattern2_weights = [self.speech_patterns2.count(speech) for speech in self.speech_patterns2]
        self.personality_traits = ["arrogant", "brave", "cowardly", "deceitful", "honest", "loyal"]
        self.mannerisms = ["nervous", "confident", "cocky", "polite", "rude"]
    
    def generate_npcs(self):
        npcs = []
        for i in range(self.num_npcs):
            race = random.choices(self.races, weights=self.race_weights, k=1)[0]
            mean_age = 30
            stdev_age = 10
            age = int(random.normalvariate(mean_age, stdev_age))
            gender = random.choices(self.genders, weights=self.gender_weights, k=1)[0]
            
            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling",
                        "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome", "deep gnome",
                        "half elf",
                        "protector aasimar", "scourge aasimar", "fallen aasimar"]:
                self.skin_color_weights = [1, 1, 1,
                                           1, 1, 1,
                                           1, 1, 1, 1,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["firbolg", "earth genasi"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           4, 4, 1, 1,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["infernal tiefling", "feral tiefling"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           4, 4, 2, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["dragonborn", "lizardfolk", "kobold"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 1, 1,
                                           1, 1, 1, 1,
                                           1, 1, 1, 1, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["half orc", "orc", "goblin"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           10, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["goliath", "triton"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 10, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["fire genasi"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 10, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["kenku"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 10, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["aarakocra"]:
                if gender in ["female"]:
                    self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 5, 
                                           5, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
                elif gender in ["male"]:
                    self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 4, 3, 3, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
                else:
                    self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 2, 
                                           3, 2, 2, 1, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["drow", "duergar"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 3, 3, 4, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 0]
            elif race in ["tabaxi"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           1, 1, 1, 1, 
                                           1, 1, 1, 1, 1, 1, 
                                           0, 0, 0]
            elif race in ["hobgoblin"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           10, 0, 0]
            elif race in ["bugbear"]:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 10, 0]
            else:
                self.skin_color_weights = [0, 0, 0,
                                           0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 0, 
                                           0, 0, 0, 0, 
                                           0, 0, 0, 0, 0, 0, 
                                           0, 0, 10]

            skin_color = random.choices(self.skin_colors, weights=self.skin_color_weights, k=1)[0]

            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
            "stout halfling", "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome",
            "deep gnome", "half elf", "protector aasimar", "scourge aasimar", "fallen aasimar", "half orc",
            "goliath", "air genasi", "earth genasi", "fire genasi", "water genasi", "duergar dwarf", "drow",
            "hobgoblin", "goblin", "yuan-ti pureblood"]:
                if gender == "female":
                    self.hair_length_weights = [4, 3, 2, 1, 0, 0]  
                elif gender == "male":
                    self.hair_length_weights = [1, 2, 3, 2, 2, 0]    
                else:
                    self.hair_length_weights = [3, 3, 3, 1, 0, 0]  
            else:
                self.hair_length_weights = [0, 0, 0, 0, 0, 10]  

            hair_length = random.choices(self.hair_lengths, weights=self.hair_length_weights, k=1)[0]
            
            if hair_length in ["no", " "]:
                self.hair_texture_weights = [0, 0, 0, 0, 4]
            else:
                self.hair_texture_weights = [1, 1, 1, 1, 0]

            hair_texture = random.choices(self.hair_textures, weights=self.hair_texture_weights, k=1)[0] 

            if hair_length in ["no", " "]:
                self.hair_color_weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 75]
            else:
                self.hair_color_weights = [25, 25, 10, 10, 1, 1, 1, 1, 1, 0]

            hair_color = random.choices(self.hair_colors, weights=self.hair_color_weights, k=1)[0]

            if age > 16:
                if gender in ["male"]:
                    self.facial_hair_weights = [2, 2, 2, 2, 2, 2]
                elif gender in ["female"]:
                    self.facial_hair_weights = [14, 0, 0, 0, 0, 0]
                else:
                    self.facial_hair_weights = [8, 1, 1, 1, 1, 1]
            else:
                self.facial_hair_weights = [14, 0, 0, 0, 0, 0]

            facial_hair = random.choices(self.facial_hairs, weights=self.facial_hair_weights, k=1)[0]

            physical_feature1 = random.choice(self.physical_features1)

            if physical_feature1 in ["with"]:
                self.physical_feature2_weights = [0, 1, 1,
                                                  1, 1, 1,
                                                  1, 1, 1,
                                                  1, 1, 1,
                                                  1, 1, 1,
                                                  1, 1, 1,
                                                  0, 0, 0,
                                                  0, 0, 0, 
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0, 0]
            elif physical_feature1 in ["missing"]:
                self.physical_feature2_weights = [0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  4, 2, 3,
                                                  4, 1, 2, 
                                                  1, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0, 0]
            elif physical_feature1 in ["scarred"]:
                self.physical_feature2_weights = [0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0, 
                                                  0, 2, 2,
                                                  2, 2, 2,
                                                  2, 1, 2, 0]
            else: 
                self.physical_feature2_weights = [17, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0, 
                                                  0, 0, 0,
                                                  0, 0, 0,
                                                  0, 0, 0, 0]

            physical_feature2 = random.choices(self.physical_features2, weights=self.physical_feature2_weights, k=1)[0]

            speech_pattern1 = random.choice(self.speech_patterns1)

            if speech_pattern1 == "with a heavy":
                self.speech_pattern2_weights = [0, 1, 1, 1, 
                                           1, 1, 1, 1] 
            else:
                self.speech_pattern2_weights = [7, 0, 0, 0,
                                           0, 0, 0, 0]
                
            speech_pattern2 = random.choices(self.speech_patterns2, weights=self.speech_pattern2_weights, k=1)[0]

            personality_trait = random.choice(self.personality_traits)
            mannerism = random.choice(self.mannerisms)
            
            npc = NewNPC(race, age, gender, skin_color, hair_length, hair_texture, hair_color, facial_hair, physical_feature1, physical_feature2, speech_pattern1, speech_pattern2, personality_trait, mannerism)
            npcs.append(npc)

        return npcs
