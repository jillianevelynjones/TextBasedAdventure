from CharClassGen import char_class_gen
from CharRaceGen import char_race_gen

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


def save_character(save_name, attributes):
    save_name_pickle = save_name + '.pickle'
    print('> saving character')
    try:
        with open(save_name_pickle, 'w') as f:
            f.write(attributes)
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

    def character_input(self, attributes_dict):

        print("\n ......................")
        print("\n First choose a race.")
        print("\n   Options are: ")
        print("     Human")
        attributes_dict["race"] = char_race_gen(attributes_dict)

        attributes_dict["class"], self.chargen_skills_proficiency_dict = char_class_gen(attributes_dict)

        print("    ......................")
        print("\n  Now we'll choose Ability Scores.")
        print("  Ability score options are 15, 14, 13, 12, 10, 8.")
        print("  You must use one of each.")
        print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")

        attributes_dict["ability scores"] = {}

        for ability in ability_scores:
            print("\n   Choose " + ability + " score:")
            while True:
                score = input("   Enter " + ability + " score: ")
                if score in score_options:
                    attributes_dict["ability scores"][ability] = score
                    score_options.remove(score)
                    print("\n   Remaining score options: " + ', '.join(score_options))
                    break
                else:
                    print("\n   Invalid " + ability + " score. Please choose from " + ', '.join(score_options))

        print("    ......................")
        print("\n    TESTING TESTING TESTING")
        print(attributes_dict)

        print("    ......................")
        print("\n Let's name your character!")
        attributes_dict['name'] = input("   Name: > ")

        self.name = attributes_dict["name"]
        self.race = attributes_dict["race"]
        self.char_class = attributes_dict["class"]
        self.ability_scores = attributes_dict["ability scores"]

        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "ability scores": ability_scores
        }

    def __init__(self):
        self.name = False
        self.race = False
        self.char_class = False
        self.ability_scores = False

    def initialize_attributes(self):
        self.name = None
        self.race = None
        self.char_class = None
        self.ability_scores = None

