class Character:
    def __init__(self):
        self.attributes_dict = {
            "size": None,
            "speed": None,
            "Languages": [],
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
        }
        return

    class Classes:

        VALID_CLASSES = ["fighter", "ranger", "paladin",
                         "wizard", "bard", "cleric",
                         "druid", "sorcerer", "warlock",
                         "monk", "rogue", "barbarian"]

        class Barbarian:
            name = "Barbarian"
            pass

        class Bard:
            pass

        class Cleric:
            pass

        class Druid:
            pass

        class Fighter:
            name = "Fighter"
            VALID_FIGHTING_STYLES = ["archery", "defense", "dueling",
                                     "greatweaponfighting", "protection", "twoweaponfighting"]
            fighter_dict = {}

            def set_fighting_style(self):

            pass

        class Monk:
            pass

        class Paladin:
            pass

        class Ranger:
            pass

        class Rogue:
            pass

        class Sorcerer:
            pass

        class Warlock:
            pass

        class Wizard:
            pass

    def calculate_ability_bonus(self):
        scores = {"str_score": self.attributes_dict["Strength"], "dex_score": self.attributes_dict["Dexterity"],
                  "con_score": self.attributes_dict["Constitution"], "int_score": self.attributes_dict["Intelligence"],
                  "wis_score": self.attributes_dict["Wisdom"], "cha_score": self.attributes_dict["Charisma"]}

        for score_name, score_value in scores.items():

            if score_value == 20:
                if score_name == "str_score":
                    str_bonus = 5
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 5
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 5
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 5
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 5
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 5
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [19, 18]:
                if score_name == "str_score":
                    str_bonus = 4
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 4
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 4
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 4
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 4
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 4
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [17, 16]:
                if score_name == "str_score":
                    str_bonus = 3
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 3
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 3
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 3
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 3
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 3
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [15, 14]:
                if score_name == "str_score":
                    str_bonus = 2
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 2
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 2
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 2
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 2
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 2
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [13, 12]:
                if score_name == "str_score":
                    str_bonus = 1
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 1
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 1
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 1
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 1
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 1
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [11, 10]:
                if score_name == "str_score":
                    str_bonus = 0
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = 0
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = 0
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = 0
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = 0
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = 0
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [9, 8]:
                if score_name == "str_score":
                    str_bonus = -1
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -1
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -1
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -1
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -1
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -1
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [7, 6]:
                if score_name == "str_score":
                    str_bonus = -2
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -2
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -2
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -2
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -2
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -2
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [5, 4]:
                if score_name == "str_score":
                    str_bonus = -3
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -3
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -3
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -3
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -3
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -3
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus

            elif score_value in [3, 2]:
                if score_name == "str_score":
                    str_bonus = -3
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -3
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -3
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -3
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -3
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -3
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus
            elif score_value == 1:
                if score_name == "str_score":
                    str_bonus = -4
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -4
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -4
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -4
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -4
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -4
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus
            else:
                if score_name == "str_score":
                    str_bonus = -5
                    self.attributes_dict["Strength_Bonus"] = str_bonus
                elif score_name == "dex_score":
                    dex_bonus = -5
                    self.attributes_dict["Dexterity_Bonus"] = dex_bonus
                elif score_name == "con_score":
                    con_bonus = -5
                    self.attributes_dict["Constitution_Bonus"] = con_bonus
                elif score_name == "int_score":
                    int_bonus = -5
                    self.attributes_dict["Intelligence_Bonus"] = int_bonus
                elif score_name == "wis_score":
                    wis_bonus = -5
                    self.attributes_dict["Wisdom_Bonus"] = wis_bonus
                elif score_name == "cha_score":
                    cha_bonus = -5
                    self.attributes_dict["Charisma_Bonus"] = cha_bonus
        return

    def get_strength_bonus(self):
        strength_bonus = self.attributes_dict["Strength_Bonus"]
        return strength_bonus

    def get_dexterity_bonus(self):
        dexterity_bonus = self.attributes_dict["Dexterity_Bonus"]
        return dexterity_bonus

    def get_constitution_bonus(self):
        constitution_bonus = self.attributes_dict["Constitution_Bonus"]
        return constitution_bonus

    def get_intelligence_bonus(self):
        intelligence_bonus = self.attributes_dict["Intelligence_Bonus"]
        return intelligence_bonus

    def get_wisdom_bonus(self):
        wisdom_bonus = self.attributes_dict["Wisdom_Bonus"]
        return wisdom_bonus

    def get_charisma_bonus(self):
        charisma_bonus = self.attributes_dict["Charisma_Bonus"]
        return charisma_bonus

    def set_strength_score(self, strength):
        self.attributes_dict["Strength"] = strength
        return

    def set_dexterity_score(self, dexterity):
        self.attributes_dict["Dexterity"] = dexterity
        return

    def set_constitution_score(self, constitution):
        self.attributes_dict["Constitution"] = constitution
        return

    def set_intelligence_score(self, intelligence):
        self.attributes_dict["Intelligence"] = intelligence
        return

    def set_wisdom_score(self, widom):
        self.attributes_dict["Wisdom"] = widom
        return

    def set_charisma_score(self, charisma):
        self.attributes_dict["Charisma"] = charisma
        return

    def set_char_name(self, name):
        self.attributes_dict["name"] = name
        return

    def set_char_race(self, race):
        self.attributes_dict["race"] = race
        return

    def set_char_language(self):
        language = input("Choose a language, your options are:" +
                         "\nCommon, Dwarvish, Elvish, Giant,\nGnomish, Goblin, Halfling, Orc,\n" +
                         "Abyssal, Celestial, Draconic, Deep Speech,\nInfernal, Primordial, Sylvan, Undercommon: ")
        self.attributes_dict["Languages"].append(language)
        return

    def set_char_class(self):
        if "classes" not in self.attributes_dict:
            self.attributes_dict["classes"] = []

        while True:
            char_class = input("Choose a class: ")
            class_name = char_class.capitalize()
            if hasattr(self.Classes, class_name):
                class_instance = getattr(self.Classes, class_name)()
                self.attributes_dict["classes"].append(class_instance)
                break
            else:
                print(f"Invalid class. Please choose from: {', '.join(self.Classes.VALID_CLASSES)}")

    def initial_attributes(self):

        self.set_char_name(input("What is your characters name? --> "))




        charisma_score = input("")


my_char = Character()

