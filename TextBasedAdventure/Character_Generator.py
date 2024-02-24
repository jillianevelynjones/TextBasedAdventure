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


def calculate_proficiency_bonus(level):
    if 1 <= level <= 4:
        prof = 2
    elif 5 <= level <= 8:
        prof = 3
    elif 9 <= level <= 12:
        prof = 4
    elif 13 <= level <= 16:
        prof = 5
    elif 17 <= level <= 20:
        prof = 6
    else:
        return prof


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


def print_character(AC, hitdice, hitpoint_max, name, size, race, level, char_class, speed, ability_scores, language1, language2, prof, skills_proficiency):
    # Name
    print("  \n   ......................")
    print("  \n   ", name)

    if size == "5":
        print("  \n   Medium ", race)
    else:
        print("  \n   Error", race)

    print("   Level ", level, char_class)

    print("  \n   ......................")

    print("  \n   Armor Class ", AC)
    print("  \n   Hit Points ", hitpoint_max, "(", level, "d", hitdice, ")")
    print("  \n   Speed ", speed, " ft.")

    print("  \n   ......................")

    print("  \n   Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"   {ability}: {score}")

    print("  \n   ......................")

    print("  \n   Proficiencies: ")
    for skill, proficiency in skills_proficiency.items():
        if proficiency:
            print("      ", skill)

    print("   Languages", language1, language2)

    print("   Proficiency Bonus +", prof)


class CharacterGenerator:
    def __init__(self):

        print("\n   ......................")
        print("You start at level 1")
        self.level = 1
        self.prof = calculate_proficiency_bonus(self.level)

        print("\n   ......................")
        print("\n   First choose a race.")
        print("   Options are: ")
        print("      Human")
        while True:
            self.race = input(f"   Enter race: ").lower()
            if self.race in ("human", "Human"):
                print("\n   As a human all your ability scores increase by 1")
                print("   Your size is medium")
                self.size = "5"
                print("   Your speed is 30")
                self.speed = "30"
                print("   You can speak, read and write in Common and one extra language of your choice")
                self.language1 = "common"
                print("\n   Your choices are: ")
                print("      Elvish")
                self.language2 = input(f"   Enter language: ")
                if self.language2 in ("elvish", "Elvish"):
                    self.language2 = "elvish"
                else:
                    print("Sorry! Only language available at the time is Elvish")
                    self.language2 = "evlish"
                break
            else:
                print("Sorry! Only human is available")
                continue
        self.char_class = char_class_gen (skills_proficiency)
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
        if self.race in ("human", "Human"):
            for ability in ability_scores:
                ability_scores[ability] = str(int(ability_scores[ability]) + 1)
        else:
            print("Error add +1 to ability scores for being human")
        self.ability_bonuses = {ability: calculate_ability_bonus(score) for ability, score in ability_scores.items()}
        print("\nFinal Ability Scores:")
        for ability, score in ability_scores.items():
            print(f"{ability}: {score} ({self.ability_bonuses[ability]})")
        self.AC = 10 + self.ability_bonuses["Dexterity"]
        self.hitdice = 10
        self.hitpoint1 = 10 + self.ability_bonuses["Constitution"]
        self.hitpoint_max = self.hitpoint1
        print("Let's name your character!")
        self.name = input("Name: > ")
        print_character(self.AC, self.hitdice, self.hitpoint_max, self.name, self.size, self.race, self.level, self.char_class, self.speed, ability_scores, self.language1, self.language2, self.prof, skills_proficiency)
        pass

    def get_attributes(self):
        return {
            "AC": self.AC,
            "Hit Dice": self.hitdice,
            "Hit Point Max": self.hitpoint_max,
            "Name": self.name,
            "Size": self.size,
            "Race": self.race,
            "Level": self.level,
            "Class": self.char_class,
            "Speed": self.speed,
            "Ability Scoes": ability_scores,
            "Language 1": self.language1,
            "Language 2": self.language2,
            "Proficiency Bonus": self.prof,
            "Skill Proficiency": skills_proficiency
        }