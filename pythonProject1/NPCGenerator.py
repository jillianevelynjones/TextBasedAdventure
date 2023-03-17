import random
from NPC import NPC
from NPCNames import NPCNames

"""Next, we'll create a class called NPCGenerator 
that will generate a list of random NPCs based on the user input"""


class NPCGenerator:
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
        self.race = random.choices(self.races, weights=self.race_weights)[0]
        self.genders = ["male", "female", "non-binary"]
        self.gender_weights = [45, 50, 5]
        self.gender = random.choices(self.genders, weights=self.gender_weights)[0]
        self.npc_names = NPCNames(race=self.race, gender=self.gender)

    def generate_npcs(self):
        physical_features1 = ["completely normal", "fat", "skinny",
                              "short", "tall", "built", "has a tattoo", "wearing glasses",
                              "missing", "scarred"]
        speech_patterns1 = ["in a normal tone", "in a soft spoken voice", "loudly",
                            "quickly", "slowly", "with a heavy accent",
                            "in a mumble", "in a stutter", "with foul language"]
        personality_traits = ["arrogant", "brave", "cowardly", "deceitful", "honest", "loyal"]
        mannerisms = ["nervous", "confident", "cocky", "polite", "rude"]

        def get_skin_color(race, gender):
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

        def get_hair_length(race, gender):
            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome",
                        "deep gnome", "half elf", "protector aasimar", "scourge aasimar", "fallen aasimar", "half orc",
                        "goliath", "air genasi", "earth genasi", "fire genasi", "water genasi", "duergar dwarf", "drow",
                        "hobgoblin", "goblin", "yuan-ti pureblood"]:
                if gender in ["female"]:
                    chair_length = random.choices(["long", "medium length", "short", "buzzed"], weights=[4, 3, 2, 1])[0]
                elif gender in ["male"]:
                    chair_length = \
                        random.choices(["long", "medium length", "short", "no hair length"], weights=[2, 3, 4, 1])[0]
                elif gender in ["non-binary"]:
                    chair_length = random.choice(["long", "medium length", "short", "no hair length"])
                else:
                    chair_length = ["error - hair length"]
            else:
                chair_length = ["no hair length"]
            return chair_length

        def get_hair_color(race):
            if race in ["human", "high elf", "wood elf",
                        "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling",
                        "forest gnome", "rock gnome", "deep gnome",
                        "half elf", "protector aasimar", "scourge aasimar",
                        "fallen aasimar"]:
                if hair_length != "no":
                    chair_color = ["no hair color"]
                else:
                    chair_color = random.choice(
                        ["brown", "black", "blonde", "ginger", "red", "orange", "green", "blue", "purple"])
            else:
                chair_color = ["no hair color"]
            return chair_color

        def get_hair_texture(hair_length):
            if hair_length != "no":
                chair_texture = random.choice(["straight", "wavy", "curly", "kinky curly"])
            else:
                chair_texture = ["no hair texture"]
            return chair_texture

        def get_facial_hair(gender, age):
            if gender in ["male"]:
                if age > 18:
                    cfacial_hair = random.choice(["a clean shaven face", "stubble", "a short beard", "a long beard",
                                                  "a mustache", "mutton chops"])
                else:
                    cfacial_hair = ["no facial hair"]
            elif gender in ["non-binary"]:
                if age > 18:
                    cfacial_hair = random.choice(["a clean shaven face", "stubble", "a short beard", "a long beard",
                                                  "a mustache", "mutton chops", "no facial hair"])
                    cfacial_weights = [1, 1, 1, 1, 1, 1, 7]
                else:
                    cfacial_hair = [" "]
            else:
                cfacial_hair = ["no facial hair"]
            return cfacial_hair

        def get_physical_feature2(physical_feature1):
            if physical_feature1 in ["completely normal", "fat", "tall", "short",
                                     "skinny", "built", "wears glasses"]:
                cphysical_feature2 = "no second physical feature"
            elif physical_feature1 in ["has a tattoo"]:
                cphysical_feature2 = random.choice(["butterfly tattoo", "rose tattoo",
                                                    "dragon tattoo", "flower tattoo", "snake tattoo",
                                                    "geometric tattoo", "lion tattoo", "heart tattoo",
                                                    "skull tattoo", "tribal tattoo", "nautical tattoo",
                                                    "moon tattoo", "pierced ear", "pierced cartilage",
                                                    "pierced nose", "eyebrow piercing", "lip piercing"])
            elif physical_feature1 in ["missing"]:
                cphysical_feature2 = random.choice(["an ear", "an arm", "a hand",
                                                    "a finger", "both arms", "a leg",
                                                    "both legs"])
            elif physical_feature1 in ["scarred"]:
                cphysical_feature2 = random.choice(["above the eye", "across the nose",
                                                    "on the cheek", "on the shoulder", "on their arm",
                                                    "on their hand", "on their back", "on their leg"])
            else:
                cphysical_feature2 = ["error - physical feature 2"]
            return cphysical_feature2

        def get_speech_pattern2(speech_pattern1):
            if speech_patterns1 in ["with a heavy accent"]:
                cspeech_pattern2 = ["midwestern accent", "english accent", "scottish accent",
                                    "russian accent", "french accent", "southern accent",
                                    "californian accent"]
            else:
                cspeech_pattern2 = ["no accent"]
            return cspeech_pattern2

        npcs = []
        for i in range(self.num_npcs):
            self.race = random.choices(self.races, weights=self.race_weights)[0]
            self.gender = random.choices(self.genders, weights=self.gender_weights)[0]
            mean_age = 35
            stdev_age = 10
            self.age = int(random.normalvariate(mean_age, stdev_age))
            self.age = max(0, min(self.age, 90))
            first_name = self.npc_names.generate_name()
            print(first_name)
            print(self.race)
            print(self.age)
            print(self.gender)
            skin_color = get_skin_color(self.race, self.gender)
            print(skin_color)
            hair_length = get_hair_length(self.race, self.gender)
            print(hair_length)
            hair_color = get_hair_color(self.race)
            print(hair_color)
            hair_texture = get_hair_texture(hair_length)
            print(hair_texture)
            facial_hair = get_facial_hair(self.gender, self.age)
            print(facial_hair)
            physical_feature1 = random.choices(physical_features1)
            print(physical_feature1)
            physical_feature2 = get_physical_feature2(physical_feature1)
            print(physical_feature2)
            speech_pattern1 = random.choices(speech_patterns1)
            print(speech_pattern1)
            speech_pattern2 = get_speech_pattern2(speech_pattern1)
            print(speech_pattern2)
            personality_trait = random.choices(personality_traits)
            print(personality_trait)
            mannerism = random.choices(mannerisms)
            print(mannerism)

            npc = NPC(first_name, self.race, self.age, self.gender,
                      skin_color, hair_length, hair_color,
                      hair_texture, facial_hair, physical_feature1,
                      physical_feature2, speech_pattern1, speech_pattern2,
                      personality_trait, mannerism)
            npcs.append(npc)
        return npcs
