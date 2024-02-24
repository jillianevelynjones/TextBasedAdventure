from char_class_gen  import char_class_gen

ability_scores = {
    "Strength": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0
}

score_options = ["15", "14", "13", "12", "10", "8"]

skills_proficiency = {
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
    "persuasion": False
}

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

    # Name
    print("  \n   ......................")
    print("  \n   ", attributes["name"])

    if attributes["size"] == "5":
        print("  \n   Medium ", attributes["race"])
    else:
        print("  \n   Error", attributes["race"])

    print("   Level ", attributes["level"], attributes["class"])

    print("  \n   ......................")

    print("  \n   Armor Class ", attributes["AC"])
    print("  \n   Hit Points ", attributes["hit point max"], "(", attributes["level"], "d", attributes["hit dice"], ")")
    print("  \n   Speed ", attributes["speed"], " ft.")

    print("  \n   ......................")

    print("  \n   Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"   {ability}: {score}")

    print("  \n   ......................")

    print("  \n   Proficiencies: ")
    for skill, proficiency in skills_proficiency.items():
        if proficiency:
            print("      ", skill)

    print("   Languages", attributes["language 1"], attributes["language 2"])

    print("   Proficiency Bonus +", attributes["proficiency bonus"])

class CharacterGenerator:
    def __init__(self):
        self.AC = False
        self.hitdice = False
        self.hitpoint = False
        self.hitpoint_max = False
        self.name = False
        self.size = False
        self.race = False
        self.level = False
        self.char_class = False
        self.speed = False
        self.ability_scores = False
        self.language1 = False
        self.language2 = False
        self.prof = False
        self.skills_proficiency = False
        self.attributes_dict = {}

    def initialize_attributes(self):
        self.AC = None
        self.hitdice = None
        self.hitpoint = None
        self.hitpoint_max = None
        self.name = None
        self.size = None
        self.race = None
        self.level = None
        self.char_class = None
        self.speed = None
        self.ability_scores = None
        self.language1 = None
        self.language2 = None
        self.prof = None
        self.skills_proficiency = None

    def get_attributes(self, attributes_dict):

        attributes = attributes_dict
        print("\n   ......................")
        print("You start at level 1")
        attributes["level"] = 1
        attributes["proficiency bonus"] = self.calculate_proficiency_bonus(attributes_dict)

        print("\n   ......................")
        print("\n   First choose a race.")
        print("   Options are: ")
        print("      Human")
        while True:
            attributes["race"] = input(f"   Enter race: ").lower()
            if attributes["race"] in ("human", "Human"):
                print("\n   As a human all your ability scores increase by 1")
                print("   Your size is medium")
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
        attributes['hit point max'] = attributes['hit point']  # Corrected syntax

        print("Let's name your character!")
        attributes['name'] = input("Name: > ")  # Corrected syntax
        print_character(attributes)

        return {
            "AC": self.AC,
            "hit dice": self.hitdice,
            "hit point": self.hitpoint,
            "hit point max": self.hitpoint_max,
            "name": self.name,
            "size": self.size,
            "race": self.race,
            "level": self.level,
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
            return self.prof
