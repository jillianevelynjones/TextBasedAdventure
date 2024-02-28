import CharInitialization 
from CharClassGen import char_class_gen
from CharRaceGen import char_race_gen

score_options = ["15", "14", "13", "12", "10", "8"]

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

    attributes_dict = CharacterInitialization.attributes_dict
    
class CharacterGenerator():

    def character_input(self, attributes_dict):

        print("\n ......................")
        print("\n First choose a race.")
        print("\n   Options are: ")
        print("     Human")
        attributes_dict["race"], self.attributes_dict = char_race_gen(attributes_dict)

        attributes_dict["class"], self.chargen_skills_proficiency_dict, self.attributes_dict = char_class_gen(attributes_dict)

        print("    ......................")
        print("\n  Now we'll choose Ability Scores.")
        print("  Ability score options are 15, 14, 13, 12, 10, 8.")
        print("  You must use one of each.")
        print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")

        ability_scores = attributes_dict["ability scores"]
        
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
            "ability scores": self.ability_scores,
            "skills proficiency": self.chargen_skills_proficiency_dict
        }
