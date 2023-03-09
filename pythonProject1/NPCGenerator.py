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
        skin_colors = ["yellow-brown umber skin", "reddish brown sepia skin", "pale brown ochre skin",
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
        skin_color_weights = [skin_colors.count(color) for color in skin_colors]
        physical_features = ["scar", "tattoo", "birthmark", "missing limb", "deformity"]
        hair_colors = ["black", "brown", "blonde", "red", "gray", "white"]
        hair_lengths = ["short", "medium", "long"]
        hair_textures = ["straight", "wavy", "curly"]
        facial_hair = ["beard", "mustache", "goatee"]
        speech_patterns = ["mumbling", "stuttering", "lisping", "accent"]
        personality_traits = ["arrogant", "brave", "cowardly", "deceitful", "honest", "loyal"]
        mannerisms = ["nervous", "confident", "cocky", "polite", "rude"]

        npcs = []
        for i in range(self.num_npcs):
            race = random.choices(races, weights=race_weights)[0]
            age = random.randint(15, 90)
            gender = random.choices(genders, weights=gender_weights)[0]
            skin_colors = random.choices(skin_colors, weights=skin_color_weights)[0]
            physical_feature = random.choice(physical_features)
            hair_color = random.choice(hair_colors)
            hair_length = random.choice(hair_lengths)
            hair_texture = random.choice(hair_textures)
            facial_hair = random.choice(facial_hair)
            speech_patterns = random.choice(speech_patterns)
            personality_traits = random.choice(personality_traits)
            mannerisms = random.choice(mannerisms)

            """to add conditions for traits based on other traits."""

            if race in ["human", "high elf", "wood elf", "eladrin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling",
                        "lightfoot halfling", "ghostwise halfling", "forest gnome", "rock gnome", "deep gnome",
                        "half elf",
                        "protector aasimar", "scourge aasimar", "fallen aasimar"]:
                skin_color = ["yellow-brown umber skin", "reddish brown sepia skin", "pale brown ochre skin",
                              "reddish brown russet skin", "brownish orange terra cotta skin", "golden skin",
                              "yellow-brown tawny skin", "gray taupe skin", "khaki colored skin",
                              "light fawn skin"]
            elif race in ["firbolg", "earth genasi"]:
                skin_color = random.choices(["brown coloring", "ruddy red coloring", "cool grays coloring",
                                             "blue coloring"], weights=[3, 3, 1, 1])[0]
            elif race in ["infernal tiefling", "feral tiefling"]:
                skin_color = random.choices(["red skin", "purple skin", "blue skin"], weights=[4, 4, 2])[0]
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

            npc = NPC(race, age, gender,
                      skin_color, physical_feature, hair_color,
                      hair_length, hair_texture, facial_hair,
                      speech_patterns, personality_traits, mannerisms)
            npcs.append(npc)
            print(f"Generated NPC {i + 1}: {npc.race} {npc.age} {npc.gender} "
                  f"{npc.skin_color} {npc.physical_feature} {npc.hair_color} "
                  f"{npc.hair_length} {npc.hair_texture} {npc.facial_hair} "
                  f"{npc.speech_patterns} {npc.personality_traits} {npc.mannerisms}")
        return npcs
