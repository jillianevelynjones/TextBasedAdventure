import TestGameMechanics


class Character:
    def __init__(self):
        self.attributes_dict = {
            "size": None,
            "speed": None,
            "Languages": [],
            "hit dice": None,
            "sub class": None,
            "proficiency bonus": 2,
            "ability bonus": None,
            "skill proficiencies": [],
            "AC": None,
            "hit points": 0,
            "light armor": False,
            "medium armor": False,
            "heavy armor": False,
            "shields": False,
            "simple weapons": False,
            "martial weapons": False,
            "strength save": 0,
            "dexterity save": 0,
            "constitution save": 0,
            "intelligence save": 0,
            "wisdom save": 0,
            "charisma save": 0,
        }
        self.set_char_name(input("What is your character's name? --> "))
        self.set_char_class()
        self.initialize_health()
        self.initialize_attribute_scores()
        self.calculate_ability_bonus()
        self.calculate_saving_throws()
        self.initialize_skill_proficiencies()
        self.calculate_skill_bonuses()
        return

    class Race:

        def __init__(self, name, stat_bonuses):
            self.name = name
            self.stat_bonuses = stat_bonuses

    class Dragonborn(Race):
        def __init__(self, dragon_type):
            super().__init__("Dragonborn", {"Strength": 2, "Charisma": 1})
            self.dragon_type = dragon_type

        def apply_breath_weapon(self):
            if self.dragon_type == "Black":
                # Apply 5 by 30 ft. line of Acid damage (Dex. save)
                # Implement logic here
                pass
            elif self.dragon_type == "Blue":
                # Apply 5 by 30 ft. line of Lightning damage (Dex. save)
                # Implement logic here
                pass
            # Add other dragon types here

    class Classes:

        VALID_CLASSES = ["fighter", "ranger", "paladin",
                         "wizard", "bard", "cleric",
                         "druid", "sorcerer", "warlock",
                         "monk", "rogue", "barbarian"]

        class Barbarian():
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 12
                self.hit_dice_num = 1

        class Bard:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 1

        class Cleric:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 1
        class Druid:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 1

        class Fighter:

            available_skills = ["Acrobatics", "Animal Handling", "Athletics",
                                "History", "Perception", "Survival"]
            strength_saving_prof = True
            constitution_saving_prof = True
            def __init__(self):
                self.level = 1
                self.fighting_style = None
                self.ranged_bonus = None
                self.ac_bonus_w_armor = None
                self.reroll_dmg = False
                self.dmg_bonus_w_single_weapon = None
                self.impose_disadvantage = False
                self.add_ability_mod_to_second_attack = False
                self.second_wind_charges = 1
                self.hit_dice_value = 10
                self.hit_dice_num = 1
                self.set_fighting_style()

            def set_fighting_style(self):
                while True:
                    print("Choose a fighting style:")
                    print("1. Archery")
                    print("2. Defense")
                    print("3. Dueling")
                    print("4. Great Weapon Fighting")
                    print("5. Protection")
                    print("6. Two-Weapon Fighting")
                    print("For a description of each type help and then the fighting style number.")
                    choice = input("Enter the number of your choice: ")
                    if choice in ["1", "help 1", "Help 1"]:
                        if choice == "1":
                            self.fighting_style = "Archery"
                            self.ranged_bonus = 2
                            break
                        else:
                            print("You gain a +2 bonus to attack rolls you make with ranged weapons.\n")
                    elif choice in ["2", "help 2", "Help 2"]:
                        if choice == "2":
                            self.fighting_style = "Defense"
                            self.ac_bonus_w_armor = 1
                            break
                        else:
                            print("While you are wearing armor, you gain a +1 bonus to AC.\n")
                    elif choice in ["3", "help 3", "Help 3"]:
                        if choice == "3":
                            self.fighting_style = "Dueling"
                            self.dmg_bonus_w_single_weapon = 2
                            break
                        else:
                            print("When you are wielding a melee weapon in one hand and no other weapons,\n" +
                                  "you gain a +2 bonus to damage rolls with that weapon.\n")
                    elif choice in ["4", "help 4", "Help 4"]:
                        if choice == "4":
                            self.fighting_style = "Great Weapon Fighting"
                            self.reroll_dmg = True
                            break
                        else:
                            print("When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon" +
                                  "\nthat you are wielding with two hands, you can reroll the die and must use the new roll," +
                                  "\neven if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile" +
                                  "\nproperty for you to gain this benefit.\n")
                    elif choice in ["5", "help 5", "Help 5"]:
                        if choice == "5":
                            self.fighting_style = "Protection"
                            self.impose_disadvantage = True
                            break
                        else:
                            print("When a creature you can see attacks a target other than you that is within 5 feet of you," +
                                  "\nyou can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.\n")
                    elif choice in ["6", "help 6", "Help 6"]:
                        if choice == "6":
                            self.fighting_style = "Two-Weapon Fighting"
                            self.add_ability_mod_to_second_attack = True
                            break
                        else:
                            print("When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.\n")
                    else:
                        print("INVALID CHOICE --- PLEASE CHOOSE AGAIN\n")
                return

            def get_fighting_style(self):
                return self.fighting_style

            def apply_archery_bonus(self):
                return

            def second_wind(self):
                fighter_level = self.level
                if self.second_wind_charges > 0:
                    total = TestGameMechanics.rolldice(self.hit_dice_value, self.hit_dice_num) + fighter_level
                    self.second_wind_charges -= 1
                else:
                    print("You have no second wind charges left.\n")

                return total

        class Monk:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 1
            pass

        class Paladin:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 10
                self.hit_dice_num = 1

        class Ranger:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 10
                self.hit_dice_num = 1

        class Rogue:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 8

        class Sorcerer:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 6
                self.hit_dice_num = 1

        class Warlock:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 8
                self.hit_dice_num = 1

        class Wizard:
            def __init__(self):
                self.level = 1
                self.hit_dice_value = 6
                self.hit_dice_num = 1

    #Calls class functions from within the classes key of the attributes_dict
    def call_classes_functions(self, function_name):
        if "classes" in self.attributes_dict:
            for char_class in self.attributes_dict["classes"]:
                if hasattr(char_class, function_name):
                    getattr(char_class, function_name)()
                else:
                    print(f"Class {char_class.__class__.__name__} does not have function {function_name}")
        return

    def calculate_saving_throws(self):
        for char_class in self.attributes_dict["classes"]:
            if hasattr(char_class, "strength_saving_prof") and char_class.strength_saving_prof:
                self.attributes_dict["strength save"] = self.attributes_dict["Strength_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["strength save"] = self.attributes_dict["Strength_Bonus"]
            if hasattr(char_class, "dexterity_saving_prof") and char_class.dexterity_saving_prof:
                self.attributes_dict["dexterity save"] = self.attributes_dict["Dexterity_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["dexterity save"] = self.attributes_dict["Dexterity_Bonus"]
            if hasattr(char_class, "constitution_saving_prof") and char_class.constitution_saving_prof:
                self.attributes_dict["constitution save"] = self.attributes_dict["Constitution_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["constitution save"] = self.attributes_dict["Constitution_Bonus"]
            if hasattr(char_class, "intelligence_saving_prof") and char_class.intelligence_saving_prof:
                self.attributes_dict["intelligence save"] = self.attributes_dict["Intelligence_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["intelligence save"] = self.attributes_dict["Intelligence_Bonus"]
            if hasattr(char_class, "wisdom_saving_prof") and char_class.wisdom_saving_prof:
                self.attributes_dict["wisdom save"] = self.attributes_dict["Wisdom_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["wisdom save"] = self.attributes_dict["Wisdom_Bonus"]
            if hasattr(char_class, "charisma_saving_prof") and char_class.charisma_saving_prof:
                self.attributes_dict["charisma save"] = self.attributes_dict["Charisma_Bonus"] + self.attributes_dict["proficiency bonus"]
            else:
                self.attributes_dict["charisma save"] = self.attributes_dict["Charisma_Bonus"]

        return

    def calculate_skill_bonuses(self):
        skills = {
            "Athletics": {"ability": "Strength_Bonus"},
            "Acrobatics": {"ability": "Dexterity_Bonus"},
            "Slight of Hand": {"ability": "Dexterity_Bonus"},
            "Stealth": {"ability": "Dexterity_Bonus"},
            "Arcana": {"ability": "Intelligence_Bonus"},
            "History": {"ability": "Intelligence_Bonus"},
            "Investigation": {"ability": "Intelligence_Bonus"},
            "Nature": {"ability": "Intelligence_Bonus"},
            "Religion": {"ability": "Intelligence_Bonus"},
            "Animal Handling": {"ability": "Wisdom_Bonus"},
            "Insight": {"ability": "Wisdom_Bonus"},
            "Medicine": {"ability": "Wisdom_Bonus"},
            "Perception": {"ability": "Wisdom_Bonus"},
            "Survival": {"ability": "Wisdom_Bonus"},
            "Deception": {"ability": "Charisma_Bonus"},
            "Intimidation": {"ability": "Charisma_Bonus"},
            "Performance": {"ability": "Charisma_Bonus"},
            "Persuasion": {"ability": "Charisma_Bonus"}
        }

        proficiency_bonus = self.attributes_dict["proficiency bonus"]

        proficiency_skills = self.attributes_dict["skill proficiencies"]
        print(f"Proficiency skills: {proficiency_skills}")

        for skill, info in skills.items():
            ability_bonus_key = info["ability"]
            ability_bonus = self.attributes_dict[ability_bonus_key]
            proficiency = skill in proficiency_skills
            skill_bonus = ability_bonus + (proficiency_bonus if proficiency else 0)
            self.attributes_dict[skill + " Bonus"] = skill_bonus

        return

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

    def initialize_health(self):
        if "classes" in self.attributes_dict:
            for char_class in self.attributes_dict["classes"]:
                if hasattr(char_class, "hit_dice_value"):
                    hit_dice_value = char_class.hit_dice_value
                    initial_health = hit_dice_value + 10
                    self.attributes_dict["hit points"] = initial_health
                else:
                    print(f"Class {char_class.__class__.__name__} does not have hit_dice_value attribute")
        return

    def initialize_attribute_scores(self):
        attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        scores = [15, 14, 13, 12, 10, 8]

        for attribute in attributes:
            print(f"Available scores for {attribute}: {scores}")
            while True:
                score = int(input(f"Choose a score for {attribute}: "))
                if score in scores:
                    scores.remove(score)
                    self.attributes_dict[attribute] = score
                    break
                else:
                    print("Invalid score. Please choose from the available scores.")
        return

    def initialize_skill_proficiencies(self):
        class_skill_choices = {
            "fighter": Character.Classes.Fighter.available_skills,
            # Add other classes and their skill choices here
        }

        if "classes" in self.attributes_dict:
            for char_class in self.attributes_dict["classes"]:
                class_name = char_class.__class__.__name__.lower()
                if class_name in class_skill_choices:
                    class_skills = class_skill_choices[class_name]
                    print(f"Choose 2 skills from {', '.join(class_skills)}:")
                    chosen_skills = []
                    while len(chosen_skills) < 2:
                        skill = input("Enter the skill name: ")
                        if skill in class_skills and skill not in chosen_skills:
                            chosen_skills.append(skill)
                        else:
                            print("Invalid skill choice. Please choose from the available skills.")
                    self.attributes_dict["skill proficiencies"].extend(chosen_skills)
                else:
                    print(f"Class {class_name} has no skill proficiencies to choose.")
        return

    def get_strength_bonus(self):
        return self.attributes_dict["Strength_Bonus"]

    def get_dexterity_bonus(self):
        return self.attributes_dict["Dexterity_Bonus"]

    def get_constitution_bonus(self):
        return self.attributes_dict["Constitution_Bonus"]

    def get_intelligence_bonus(self):
        return self.attributes_dict["Intelligence_Bonus"]

    def get_wisdom_bonus(self):
        return self.attributes_dict["Wisdom_Bonus"]

    def get_charisma_bonus(self):
        return self.attributes_dict["Charisma_Bonus"]

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
        return


my_char = Character()
print(my_char.attributes_dict)
