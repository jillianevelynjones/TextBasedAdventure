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
        skin_colors = ["pale", "fair", "tan", "olive", "brown", "dark"]
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
            skin_colors = random.choice(skin_colors)
            physical_feature = random.choice(physical_features)
            hair_color = random.choice(hair_colors)
            hair_length = random.choice(hair_lengths)
            hair_texture = random.choice(hair_textures)
            facial_hair = random.choice(facial_hair)
            speech_patterns = random.choice(speech_patterns)
            personality_traits = random.choice(personality_traits)
            mannerisms = random.choice(mannerisms)

            """to add conditions for traits based on other traits."""

            if race in ["human", "high elf", "wood elf",
                        "eldarin elf", "hill dwarf", "mountain dwarf",
                        "stout halfling", "lightfoot halfling", "ghostwise halfling",
                        "forest gnome", "rock gnome", "deep gnome",
                        "half elf", "protector aasimar", "scourge aasimar",
                        "fallen aasimar"]:
                skin_colors = ["yellow-brown umber", "reddish brown sepia",
                               "pale brown ochre", "reddish brown russet",
                               "brownish orange terra cotta", "gold",
                               "yellow-brown tawny", "gray taupe",
                               "khaki", "light fawn"]
            elif race in ["firbolg", "elf genasi"]:
                skin_colors = ["brown", "ruddy red", "cool grays", "blue"]
                skin_color_weights = [3, 3, 1, 1]
            else:
                skin_colors = ["1", "2", "3", "4", "5", "6"]

            skin_colors = random.choice(skin_colors)


            npc = NPC(race, age, gender,
                      skin_colors, physical_feature, hair_color,
                      hair_length, hair_texture, facial_hair,
                      speech_patterns, personality_traits, mannerisms)
            npcs.append(npc)
            print(f"Generated NPC {i + 1}: {npc.race} {npc.age} {npc.gender} {npc.skin_color} {npc.physical_feature} {npc.hair_color} {npc.hair_length} {npc.hair_texture} {npc.facial_hair} {npc.speech_patterns} {npc.personality_traits} {npc.mannerisms}")
        return npcs
