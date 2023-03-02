import random
from NPC import NPC


"""Next, we'll create a class called NPCGenerator 
that will generate a list of random NPCs based on the user input"""


class NPCGenerator:
    def __init__(self, race, gender, num_npcs):
        self.num_npcs = num_npcs
        self.npcs = []
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
                            "gray feathers", "red feathers", "yellow feathers", "orange feathers",
                            "error - aarakocra skin", "dark gray skin", "light gray skin", "gray skin",
                            "black fur with white spots", "yellow fur", "orange fur", "yellow fur with orange stripes",
                            "black fur", "white fur", "calico fur", "brown fur", "cinnamon fur", "gray fur",
                            "orange skin with a blue nose", "brown fur", "error - skin color races"]
        self.skin_color_weights = []
        self.hair_lengths = ["long", "medium length", "short", "buzzed", "no", "error - hair length"]
        self.hair_length_weights = []
        self.hair_colors = ["brown", "black", "blonde", "ginger", "red", "orange", "green", "blue", "purple"]
        self.hair_color_weights = []
        self.hair_textures = ["straight", "wavy", "curly", "kinky curly"]
        self.hair_texture_weights = []
        self.facial_hairs = [" ", "stubble", "a short beard", "a long beard", "a mustache", "mutton chops"]
        self.facial_hair_weights = []
        self.physical_features1 = ["completely normal", " ", "fat", "skinny",
                                   "short", "tall", "built", "wearing glasses",
                                   "missing", "scarred"]
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
        self.speech_patterns1 = ["in a normal tone", "in a soft spoken voice", "loudly",
                                 "quickly", "slowly", "with a heavy",
                                 "in a mumble", "in a stutter", "with foul language"]
        self.speech_patterns2 = ["midwestern accent", "english accent", "scottish accent",
                                 "russian accent", "french accent", "southern accent",
                                 "californian accent"]
        self.personality_traits = ["arrogant", "brave", "cowardly", "deceitful", "honest", "loyal"]
        self.mannerisms = ["nervous", "confident", "cocky", "polite", "rude"]
        self.name = NPCNames.generate_name(self.race, self.gender)

    def generate_npcs(self):
        npcs = []
        for i in range(self.num_npcs):
            race = random.choices(self.races, weights=self.race_weights)[0]
            age = random.randint(15, 90)
            gender = random.choices(self.genders, weights=self.gender_weights)[0]
            skin_color = random.choices(self.skin_colors, weights=self.skin_color_weights)[0]
            physical_feature1 = random.choice(self.physical_features1)
            physical_feature2 = random.choice(self.physical_features2)
            hair_color = random.choices(self.hair_colors, weights=self.hair_color_weights)[0]
            hair_length = random.choices(self.hair_lengths, weights=self.hair_length_weights)[0]
            hair_texture = random.choices(self.hair_textures, weights=self.hair_texture_weights)[0]
            facial_hair = random.choices(self.facial_hairs, weights=self.facial_hair_weights)[0]
            speech_patterns1 = random.choice(self.speech_patterns1)
            speech_patterns2 = random.choice(self.speech_patterns2)
            personality_traits = random.choice(self.personality_traits)
            mannerisms = random.choice(self.mannerisms)

            """to add conditions for traits based on other traits."""

            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf", "stout halfling",
                        "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome", "deep gnome", "half elf",
                        "protector aasimar", "scourge aasimar", "fallen aasimar"]:
                skin_color = ["yellow-brown umber skin", "reddish brown sepia skin", "pale brown ochre skin",
                              "reddish brown russet skin", "brownish orange terra cotta skin", "golden skin",
                              "yellow-brown tawny skin", "gray taupe skin", "khaki colored skin", "light fawn skin"]
            elif race in ["firbolg", "earth genasi"]:
                skin_color = ["brown coloring", "ruddy red coloring",
                              "cool grays coloring", "blue coloring"]
                skin_color_weights = [3, 3, 1, 1]
            elif race in ["infernal tiefling", "feral tiefling"]:
                skin_color = ["red skin", "purple skin", "blue skin"]
                skin_color_weights = [4, 4, 2]
            elif race in ["dragonborn", "lizardfolk", "kobold"]:
                skin_color = ["red coloring", "blue coloring", "green coloring",
                              "black coloring", "white coloring", "copper coloring",
                              "brass coloring", "silver coloring", "gold coloring",
                              "bronze coloring"]
            elif race in ["half orc", "orc", "goblin"]:
                skin_color = ["green skin"]
            elif race in ["goliath", "triton"]:
                skin_color = ["grayish blue skin"]
            elif race in ["fire genasi"]:
                skin_color = ["red skin"]
            elif race in ["kenku"]:
                skin_color = ["black feathers"]
            elif race in ["aarakocra"]:
                if gender in ["female"]:
                    skin_color = ["brown feathers", "gray feathers"]
                elif gender in ["male"]:
                    skin_color = ["red feathers", "yellow feathers", "orange feathers"]
                else:
                    skin_color = ["red feathers", "yellow feathers", "orange feathers",
                                  "brown feathers", "gray feathers"]
            elif race in ["drow", "duergar"]:
                skin_color = ["dark gray skin", "light gray skin", "gray skin"]
            elif race in ["tabaxi"]:
                skin_color = ["black fur with white spots", "yellow fur", "orange fur",
                              "yellow fur with orange stripes", "black fur", "white fur",
                              "calico fur", "brown fur", "cinnamon fur", "gray fur"]
            elif race in ["hobgoblin"]:
                skin_color = ["orange skin with a blue nose"]
            elif race in ["bugbear"]:
                skin_color = ["brown fur"]
            else:
                skin_color = ["error - skin color races"]

            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome",
                        "deep gnome", "half elf", "protector aasimar", "scourge aasimar", "fallen aasimar", "half orc",
                        "goliath", "air genasi", "earth genasi", "fire genasi", "water genasi", "duergar dwarf", "drow",
                        "hobgoblin", "goblin", "yuan-ti pureblood"]:
                if gender in ["female"]:
                    hair_length = ["long", "medium length", "short", "buzzed"]
                    hair_lengths_weights = [4, 3, 2, 1]
                elif gender in ["male"]:
                    hair_length = ["long", "medium length", "short", "no"]
                    hair_lengths_weights = [2, 3, 4, 1]
                elif gender in ["non binary"]:
                    hair_length = ["long", "medium length", "short", "no"]
                else:
                    hair_length = ["error - hair length"]
            else:
                hair_length = [" "]

            if race in ["human", "high elf", "wood elf",
                        "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling",
                        "forest gnome", "rock gnome", "deep gnome",
                        "half elf", "protector aasimar", "scourge aasimar",
                        "fallen aasimar"]:
                if hair_length != "no":
                    hair_texture = [" "]
                else:
                    hair_texture = ["straight", "wavy", "curly", "kinky curly"]

            if gender in ["male"]:
                facial_hair = ["a clean shaven face", "stubble", "a short beard", "a long beard", "a mustache", "mutton chops"]
                facial_hair_weights = [20, 10, 5, 5, 1, 1]
            elif gender in ["non binary"]:
                facial_hair = [" ", "stubble", "a short beard", "a long beard", "a mustache", "mutton chops"]
                facial_hair_weights = [50, 1, 1, 1, 1, 1]
            else:
                facial_hair = [" "]

            if physical_feature1 in ["completely normal", "fat",
                                     "skinny", "built", "wears glasses"]:
                physical_feature2 = " "
            elif physical_feature2 in [" "]:
                physical_feature2 = ["butterfly tattoo", "rose tattoo",
                                     "dragon tattoo", "flower tattoo", "snake tattoo",
                                     "geometric tattoo", "lion tattoo", "heart tattoo",
                                     "skull tattoo", "tribal tattoo", "nautical tattoo",
                                     "moon tattoo", "pierced ear", "pierced cartilage",
                                     "pierced nose", "eyebrow piercing", "lip piercing"]
            elif physical_feature1 in ["missing"]:
                physical_feature2 = ["an ear", "an arm", "a hand",
                                   "a finger", "both arms", "a leg",
                                   "both legs"]
            elif physical_feature1 in ["scarred"]:
                physical_feature2 = ["above the eye", "across the nose",
                                   "on the cheek", "on the shoulder", "on their arm",
                                   "on their hand", "on their back", "on their leg"]
            else:
                physical_feature2 = ["error - physical feature 2"]

            if speech_pattern1 in ["with a heavy"]:
                speech_pattern2 = ["midwestern accent", "english accent", "scottish accent",
                                   "russian accent", "french accent", "southern accent",
                                   "californian accent"]
            else:
                speech_pattern2 = [" "]

            npc = NPC(race, age, gender, skin_color,
                      physical_feature1, physical_feature2, hair_color,
                      hair_length, hair_texture, facial_hair,
                      speech_pattern1, speech_pattern2, personality_traits,
                      mannerisms)
            npcs.append(npc)

        self.npcs = npcs
        return npcs