from CharClassGen import char_class_gen

ability_scores = {
  "Strength": 0,
  "Dexterity": 0,
  "Constitution": 0,
  "Intelligence": 0,
  "Wisdom": 0,
  "Charisma": 0
}

score_options = ["15", "14", "13", "12", "10", "8"]


def initialize_char_skills_prof():
    char_initial_skills_proficiency_dict = {
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
        "": False
    }
    return char_initial_skills_proficiency_dict


char_skills_proficiency_dict = initialize_char_skills_prof()
    

def calculate_ability_bonus(score):
    if score == "20":
        return 5
    elif score in ["18", "19"]:
        return 4
    elif score in ["16", "17"]:
        return 3
    elif score in ["14", "15"]:
        return 2
    elif score in ["12", "13"]:
        return 1
    elif score in ["10", "11"]:
        return 0
    elif score in ["8", "9"]:
        return -1
    elif score in ["6", "7"]:
        return -2
    elif score in ["4", "5"]:
        return -3
    elif score in ["2", "3"]:
        return -4
    elif score == "1":
        return -5
    else:
        return None


def print_character(attributes_dict):
    attributes = attributes_dict
    
    character_generator = CharacterGenerator()

    print("  \n  ......................")
    print("  \n  ", attributes["name"])

    if attributes["size"] == "5":
        print("  \n   Medium ", attributes["race"])
    else:
        print("  \n  Error", attributes["race"])

    print("   Level ", attributes["level"], attributes["class"])

    print("  \n  ......................")

    print("  \n  Armor Class ", attributes["AC"])
    print("  \n  Hit Point Max ", attributes["hit point max"], " (", attributes["level"], "d", attributes["hit dice"], ")")
    print("  \n  Speed ", attributes["speed"], " ft.")

    print("  \n  ......................")

    print("\n  Ability Scores: ")
    for ability, score in attributes["ability scores"].items():
        print(f"   {ability}: {score}")

    print("  \n  ......................")

    print("  \n  Proficiencies: ")
    for skill, proficiency in attributes["skills proficiency"].items():
        if proficiency:
            print("   ", skill)
            skill_bonuses = character_generator.calculate_skill_bonuses(attributes["ability scores"], attributes["proficiency bonus"], attributes["skills proficiency"])
            print_skill_bonuses(skill_bonuses)

    print("   Languages", attributes["language 1"], attributes["language 2"])

    print("   Proficiency Bonus +", attributes["proficiency bonus"])


def save_character(save_name, character_sheet):
    save_name_pickle = save_name + '.pickle'
    print('> saving character')
    try:
        with open(save_name_pickle, 'w') as f:
            f.write(character_sheet)
        print('> character saved successfully')
    except Exception as e:
        print('> error saving character:', e)


def assign_skills_to_ability(char_skills_proficiency_dict):
    skill_ability_map = {
      "athletics": "Strength",
      "acrobatics": "Dexterity",
      "sleight of hand": "Dexterity",
      "stealth": "Dexterity",
      "arcana": "Intelligence",
      "history": "Intelligence",
      "investigation": "Intelligence",
      "nature": "Intelligence",
      "religion": "Intelligence",
      "animal handling": "Wisdom",
      "insight": "Wisdom",
      "medicine": "Wisdom",
      "perception": "Wisdom",
      "survival": "Wisdom",
      "deception": "Charisma",
      "intimidation": "Charisma",
      "performance": "Charisma",
      "persuasion": "Charisma"
    }
    return {skill: skill_ability_map[skill] for skill in char_skills_proficiency_dict}


def print_skill_bonuses(skill_bonuses):
    for skill, bonus in skill_bonuses.items():
        if bonus > 0:
            print("  ", skill, " +", bonus)
        elif bonus == 0:
            print("  ", skill, " ", bonus)
        else:
            print("  ", skill, " -", abs(bonus))


class CharacterGenerator():

    skills_proficiency = initialize_char_skills_prof()

    def calculate_proficiency_bonus(self, attributes_dict):
        self.attributes = attributes_dict
        if 1 <= self.attributes["level"] <= 4:
            return 2
        elif 5 <= self.attributes["level"] <= 8:
            return 3
        elif 9 <= self.attributes["level"] <= 12:
            return 4
        elif 13 <= self.attributes["level"] <= 16:
            return 5
        elif 17 <= self.attributes["level"] <= 20:
            return 6
        else:
            return None

    def calculate_skill_bonuses(self, ability_scores, proficiency_bonus, chargen_skills_proficiency_dict):
        skill_ability_map = assign_skills_to_ability(chargen_skills_proficiency_dict)
        skill_bonuses = {}

        for skill, ability in skill_ability_map.items():
            ability_bonus = calculate_ability_bonus(ability_scores[ability])
            proficiency_bonus_with_ability = proficiency_bonus + ability_bonus
            skill_bonuses[skill] = proficiency_bonus_with_ability

        return skill_bonuses

    def get_attributes(self, attributes_dict, chargen_skills_proficiency_dict):

        attributes = attributes_dict
        print("\n ......................")
        print("\n You start at level 1")
        attributes["level"] = 1
        print("\n ......................")
        print("\n First choose a race.")
        print("\n   Options are: ")
        print("     Human")
        while True:
            attributes["race"] = input(f"\n   Enter race: ").lower()
            if attributes["race"] in ("human", "Human"):
                print("\n   As a human all your ability scores increase by 1")
                print("\n Your size is medium")
                attributes["size"] = "5"
                print("   Your speed is 30")
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

        attributes["proficiency bonus"] = self.calculate_proficiency_bonus(attributes)

        attributes["class"], self.chargen_skills_proficiency_dict = char_class_gen(attributes_dict)
        print("    ......................")
        print("\n  TESTING AFTER FIGHTER FUNCTION ", self.chargen_skills_proficiency_dict)

        attributes["skills proficiency"] = chargen_skills_proficiency_dict

        print("    ......................")
        print("\n  TESTING PASSING TO ATTRIBUTES ", attributes["skills proficiency"])

        print("    ......................")
        print("\n  Now we'll choose Ability Scores.")
        print("  Ability score options are 15, 14, 13, 12, 10, 8.")
        print("  You must use one of each.")
        print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")

        attributes["ability scores"] = {}

        for ability in ability_scores:
            print("\n   Choose " + ability + " score:")
            while True:
                score = input("   Enter " + ability + " score: ")
                if score in score_options:
                    attributes["ability scores"][ability] = score
                    score_options.remove(score)
                    print("\n   Remaining score options: " + ', '.join(score_options))
                    break
                else:
                    print("\n   Invalid " + ability + " score. Please choose from " + ', '.join(score_options))

        attributes["ability bonuses"] = {ability: calculate_ability_bonus(score) for ability, score in attributes["ability scores"].items()}
        
        if attributes["race"] in ("human", "Human"):
            print('\n   Humans get a +1 to all ability scores')
            for ability in attributes["ability scores"]:
                attributes["ability scores"][ability] = str(int(attributes["ability scores"][ability]) + 1)
        else:
            print("Error: add +1 to ability scores for being human")
        
        print("\n   Final Ability Scores:")
        for ability, score in attributes["ability scores"].items():
            print("   ", ability + ": " + str(score) + " (" + str(attributes['ability bonuses'][ability]) + ")")

        attributes['AC'] = str(10 + int(attributes['ability bonuses']['Dexterity']))
        attributes['hit point lvl 1'] = str(10 + int(attributes['ability bonuses']['Constitution']))
        if attributes["level"] == 1:
            attributes["hit point max"] = attributes["hit point lvl 1"]
        else:
            print("hit point max / level one error")

        print("\n Let's name your character!")
        attributes['name'] = input("   Name: > ")

        self.name = attributes["name"]
        self.size = attributes["size"]
        self.race = attributes["race"]
        self.level = attributes["level"]
        self.AC = attributes["AC"]
        self.hitdice = attributes["hit dice"]
        self.hitpoint_max = attributes["hit point max"]
        self.char_class = attributes["class"]
        self.speed = attributes["speed"]
        self.ability_scores = attributes["ability scores"]
        self.language1 = attributes["language 1"]
        self.language2 = attributes["language 2"]
        self.prof = attributes["proficiency bonus"]
        self.chargen_skills_proficiency_dict = attributes["skills proficiency"]
        self.ability_bonuses = attributes["ability bonuses"]
        self.level1HP = attributes["hit point lvl 1"]

        print_character(attributes)

        return {
            "name": self.name,
            "size": self.size,
            "race": self.race,
            "level": self.level,
            "AC": self.AC,
            "hit dice": self.hitdice,
            "hit point": self.hitpoint,
            "hit point max": self.hitpoint_max,
            "class": self.char_class,
            "speed": self.speed,
            "ability scores": ability_scores,
            "language 1": self.language1,
            "language 2": self.language2,
            "proficiency bonus": self.prof,
            "skills proficiency": self.skills_proficiency,
            "ability bonuses": self.ability_bonuses,
            "hit point lvl 1": self.level1HP
        }

    def __init__(self):
        self.name = False
        self.size = False
        self.race = False
        self.level = False
        self.AC = False
        self.hitdice = False
        self.hitpoint = False
        self.hitpoint_max = False
        self.char_class = False
        self.speed = False
        self.ability_scores = False
        self.language1 = False
        self.language2 = False
        self.prof = False
        self.chargen_skills_proficiency_dict = False
        self.ability_bonuses = False
        self.level1HP = False
        self.attributes_dict = False

    def initialize_attributes(self):
        self.name = None
        self.size = None
        self.race = None
        self.level = None
        self.AC = None
        self.hitdice = None
        self.hitpoint = None
        self.hitpoint_max = None
        self.char_class = None
        self.speed = None
        self.ability_scores = None
        self.language1 = None
        self.language2 = None
        self.prof = None
        self.chargen_skills_proficiency_dict = None
        self.ability_bonuses = None
        self.level1HP = None
