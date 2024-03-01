attributes_dict = {
    "name": None,
    "race": None,
    "size": None,
    "speed": None,
    "language 1": None,
    "language 2": None,
    "class": None,
    "hit dice": None,
    "sub class": None,
    "proficiency bonus": None,
    "ability bonus": None,
    "skill bonus": None,
    "AC": None,
    "hit point lvl 1": None,
    "light armor": False,
    "medium armor": False,
    "heavy armor": False,
    "shields": False,
    "simple weapons": False,
    "martial weapons": False,
    "strength save": False,
    "dexterity save": False,
    "constitution save": False,
    "intelligence save": False,
    "wisdom save": False,
    "charisma save": False,
    "athletics": False,
    "acrobatics": False,
    "sleight of hand": False,
    "stealth": False,
    "arcana": False,
    "history": False,
    "investigation": False,
    "nature": False,
    "religion": False,
    "animal handling": False,
    "insight": False,
    "medicine": False,
    "perception": False,
    "survival": False,
    "deception": False,
    "intimidation": False,
    "performance": False,
    "persuasion": False,
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0
}

def calculate_ability_bonus():
    scores = {"str_score": attributes_dict["Strength"], "dex_score": attributes_dict["Dexterity"],
              "con_score": attributes_dict["Constitution"], "int_score": attributes_dict["Intelligence"],
              "wis_score": attributes_dict["Wisdom"], "cha_score": attributes_dict["Charisma"]}

    for score_name, score_value in scores.items():

        if score_value == 20:
            if score_name == "str_score":
                str_bonus = 5
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 5
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 5
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 5
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 5
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 5
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [19, 18]:
            if score_name == "str_score":
                str_bonus = 4
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 4
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 4
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 4
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 4
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 4
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [17, 16]:
            if score_name == "str_score":
                str_bonus = 3
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 3
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 3
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 3
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 3
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 3
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [15, 14]:
            if score_name == "str_score":
                str_bonus = 2
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 2
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 2
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 2
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 2
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 2
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [13, 12]:
            if score_name == "str_score":
                str_bonus = 1
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 1
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 1
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 1
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 1
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 1
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [11, 10]:
            if score_name == "str_score":
                str_bonus = 0
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = 0
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = 0
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = 0
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = 0
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = 0
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [9, 8]:
            if score_name == "str_score":
                str_bonus = -1
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -1
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -1
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -1
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -1
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -1
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [7, 6]:
            if score_name == "str_score":
                str_bonus = -2
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -2
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -2
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -2
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -2
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -2
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [5, 4]:
            if score_name == "str_score":
                str_bonus = -3
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -3
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -3
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -3
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -3
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -3
                attributes_dict["Charisma_Bonus"] = cha_bonus

        elif score_value in [3, 2]:
            if score_name == "str_score":
                str_bonus = -3
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -3
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -3
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -3
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -3
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -3
                attributes_dict["Charisma_Bonus"] = cha_bonus
        elif score_value == 1:
            if score_name == "str_score":
                str_bonus = -4
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -4
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -4
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -4
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -4
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -4
                attributes_dict["Charisma_Bonus"] = cha_bonus
        else:
            if score_name == "str_score":
                str_bonus = -5
                attributes_dict["Strength_Bonus"] = str_bonus
            elif score_name == "dex_score":
                dex_bonus = -5
                attributes_dict["Dexterity_Bonus"] = dex_bonus
            elif score_name == "con_score":
                con_bonus = -5
                attributes_dict["Constitution_Bonus"] = con_bonus
            elif score_name == "int_score":
                int_bonus = -5
                attributes_dict["Intelligence_Bonus"] = int_bonus
            elif score_name == "wis_score":
                wis_bonus = -5
                attributes_dict["Wisdom_Bonus"] = wis_bonus
            elif score_name == "cha_score":
                cha_bonus = -5
                attributes_dict["Charisma_Bonus"] = cha_bonus
    return

def get_strength_bonus():
    strength_bonus = attributes_dict["Strength_Bonus"]
    return strength_bonus

def get_dexterirty_bonus():
    dexterity_bonus = attributes_dict["Dexterity_Bonus"]
    return dexterity_bonus

def get_constition_bonus():
    constitution_bonus = attributes_dict["Constitution_Bonus"]
    return constitution_bonus

def get_intelligence_bonus():
    intelligence_bonus = attributes_dict["Intelligence_Bonus"]
    return intelligence_bonus

def get_wisdom_bonus():
    wisdom_bonus = attributes_dict["Wisdom_Bonus"]
    return wisdom_bonus

def get_charisma_bonus():
    charisma_bonus = attributes_dict["Charisma_Bonus"]
    return charisma_bonus

def set_strength_score():
    strength_score = attributes_dict["Strength"]
    return strength_score

def set_dexterity_score():
    dexterity_score = attributes_dict["Dexterity"]
    return dexterity_score

def set_constitution_score():
    constitution_score = attributes_dict["Constitution"]
    return constitution_score

def set_intelligence_score():
    intelligence_score = attributes_dict["Intelligence"]
    return intelligence_score

def set_wisdom_score():
    wisdom_score = attributes_dict["Wisdom"]
    return wisdom_score

def set_charisma_score():
    charisma_score = attributes_dict["Charisma"]
    return charisma_score


class CharacterGenerator:
    def __init__(self):
        self.name = None
        self.race = None
        self.size = None
        self.speed = None
        self.language_1 = None
        self.language_2 = None
        self.char_class = None
        self.hit_dice = None
        self.sub_class = None
        self.proficiency_bonus = None
        self.ability_bonus = None
        self.skill_bonus = None
        self.AC = None
        self.hp = None
        self.light_armor = False
        self.medium_armor = False
        self.heavy_armor = False
        self.shields = False
        self.simple_weapons = False
        self.martial_weapons = False
        self.strength_save = False
        self.dexterity_save = False
        self.constitution_save = False
        self.intelligence_save = False
        self.wisdom_save = False
        self.charisma_save = False
        self.athletics = False
        self.acrobatics = False
        self.sleight_of_hand = False
        self.stealth = False
        self.arcana = False
        self.history = False
        self.investigation = False
        self.nature = False
        self.religion = False
        self.animal_handling = False
        self.insight = False
        self.medicine = False
        self.perception = False
        self.survival = False
        self.deception = False
        self.intimidation = False
        self.performance = False
        self.persuasion = False
        self.Strength = None
        self.Dexterity = None
        self.Constitution = None
        self.Intelligence = None
        self.Wisdom = None
        self.Charisma = None

    def get_attributes(self, attributes_dict):

        attributes = attributes_dict
        print("\n   ......................")
        print("You start at level 1")
        attributes["level"] = 1
        # attributes["proficiency bonus"] = self.calculate_proficiency_bonus(attributes_dict)

        print("\n   ......................")
        print("\n   First choose a race.")
        print("   Options are: ")
        print("      Human")
        while True:
            attributes["race"] = input(f"   Enter race: ").lower()
            if attributes["race"] in ("human", "Human"):
                # print("\n   As a human all your ability scores increase by 1")
                print("   Your size is medium")
                attributes["size"] = "5"
                break

        self.name = attributes["name"]
        self.size = attributes["size"]

        '''print("   Your speed is 30")
        attributes["speed"] = "30"
        print("   You can speak, read and write in Common and one extra language of your choice")
        attributes["language 1"] = "common"
        print("\n   Your choices are: ")
        print("      Elvish")
        attributes["language 2"] = input(f"   Enter language: ")
        if attributes["language 2"] in ("elvish", "Elvish"):
            attributes["language 2"] = "elvish"
        else:
            print("Sorry! Only language available at the time is Elvish")
            attributes["language 2"] = "elvish"
        break
    else:
        print("Sorry! Only human is available")
        continue
        attributes["class"] = char_class_gen (skills_proficiency)
        print("    ......................")
        print("\n  Now we'll choose Ability Scores.")
        print("  Ability score options are 15, 14, 13, 12, 10, 8.")
        print("  You must use one of each.")
        print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")
        for ability in ability_scores:

            print(f"\n   Choose {ability} score:")
            while True:
                score = input(f"   Enter {ability} score: ")
                if score in score_options:
                    ability_scores[ability] = score
                    score_options.remove(score)
                    print(f"\n   Remaining score options: {', '.join(score_options)}")
                    break
                else:
                    print(f"\n   Invalid {ability} score. Please choose from {', '.join(score_options)}.")
        if attributes["race"] in ("human", "Human"):
            for ability in ability_scores:
                ability_scores[ability] = str(int(ability_scores[ability]) + 1)
        else:
            print("Error add +1 to ability scores for being human")
        attributes["ability_bonuses"] = {ability: calculate_ability_bonus(score) for ability, score in ability_scores.items()}
        print("\nFinal Ability Scores:")
        for ability, score in ability_scores.items():
            print(f"{ability}: {score} ({attributes['ability_bonuses'][ability]})")  # Corrected syntax

        attributes['AC'] = 10 + attributes['ability_bonuses']['Dexterity']  # Corrected syntax
        attributes['hit dice'] = 10  # Corrected syntax
        attributes['hit point'] = 10 + attributes['ability_bonuses']['Constitution']  # Corrected syntax
        attributes['hit point max'] = attributes['hit point']  # Corrected syntax'''

        print("Let's name your character!")
        attributes['name'] = input("Name: > ")  # Corrected syntax
        print_character(attributes)

        return {
            "name": self.name,
            "size": self.size,
            "race": self.race,
            "level": self.level
        }

    ''''"AC": self.AC,
        "hit dice": self.hitdice,
        "hit point": self.hitpoint,
        "hit point max": self.hitpoint_max,


        "class": self.char_class,
        "speed": self.speed,
        "ability scores": ability_scores,
        "language 1": self.language1,
        "language 2": self.language2,
        "proficiency bonus": self.prof,
        "skill proficiency": skills_proficiency
    }

    def calculate_proficiency_bonus(self, attributes_dict):
        attributes = attributes_dict
        if 1 <= attributes["level"] <= 4:
            self.prof = 2
        elif 5 <= attributes["level"] <= 8:
            self.prof = 3
        elif 9 <= attributes["level"] <= 12:
            self.prof = 4
        elif 13 <= attributes["level"] <= 16:
            self.prof = 5
        elif 17 <= attributes["level"] <= 20:
            self.prof = 6
        else:
            return self.prof'''

print(calculate_ability_bonus())
print(get_strength_bonus())
