from charClass_gen import charClass_gen
def character_generator():
    ability_scores = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    score_options = ["15", "14", "13", "12", "10", "8"]

    light_armor = False,
    medium_armor = False
    heavy_armor = False
    shields = False
    simple_weapon = False
    martial_weapon = False
    STRsaveprof = False
    DEXsaveprof = False
    CONsaveprof = False
    INTsaveprof = False
    WISsaveprof = False
    CHAsaveprof = False
    athletics = False
    acrobatics = False
    sleight_of_hand = False
    stealth = False
    arcana = False
    history = False
    investigation = False
    nature = False
    religion = False
    animal_handling = False
    insight = False
    medicine = False
    perception = False
    survival = False
    deception = False
    intimidation = False
    performance = False
    persuasion = False

    skills_proficiency = {
        "light armor": light_armor,
        "medium armor": medium_armor,
        "heavy armor": heavy_armor,
        "shields": shields,
        "simple weapons": simple_weapon,
        "martial weapons": martial_weapon,
        "strength save": STRsaveprof,
        "dexterity save": DEXsaveprof,
        "constitution save": CONsaveprof,
        "intelligence save": INTsaveprof,
        "wisdom save": WISsaveprof,
        "charisma save": CHAsaveprof,
        "athletics": athletics,
        "acrobatics": acrobatics,
        "sleight of hand": sleight_of_hand,
        "stealth": stealth,
        "arcana": arcana,
        "history": history,
        "investigation": investigation,
        "nature": nature,
        "religion": religion,
        "animal handling": animal_handling,
        "insight": insight,
        "medicine": medicine,
        "perception": perception,
        "survival": survival,
        "deception": deception,
        "intimidation": intimidation,
        "performance": performance,
        "persuasion": persuasion
    }

    print("  \n   ......................")
    print("You start at level 1")
    level = 1

    prof = calculate_proficiency_bonus(level)

    print("  \n   ......................")
    print("  \n   First choose a race.")
    print("   Options are: ")
    print("      Human")
    while True:
        race = input(f"   Enter race: ").lower()
        if race in ("human", "Human"):
            print("  \n   As a human all your ability scores increase by 1")
            print("   Your size is medium")
            size = "5"
            print("   Your speed is 30")
            speed = "30"
            print("   You can speak, read and write in Common and one extra language of your choice")
            language1 = ("common")
            print("  \n   Your choices are: ")
            print("      Elvish")
            language2 = input(f"   Enter language: ")
            if language2 in ("elvish", "Elvish"):
                language2 = ("elvish")
            else:
                print("Sorry! Only language available at the time is Elvish")
                language2 = ("evlish")
            break
        else:
            print("Sorry! Only human is available")
            continue

    CharClass = charClass_gen(skills_proficiency)

    print("   \n   ......................")
    print("  \n  Now we'll choose Ability Scores.")
    print("  Ability score options are 15, 14, 13, 12, 10, 8.")
    print("  You must use one of each.")
    print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")

    for ability in ability_scores:

        print(f"  \n   Choose {ability} score:")
        while True:
            score = input(f"   Enter {ability} score: ")
            if score in score_options:
                ability_scores[ability] = score
                score_options.remove(score)
                print(f"  \n   Remaining score options: {', '.join(score_options)}")
                break
            else:
                print(f"  \n   Invalid {ability} score. Please choose from {', '.join(score_options)}.")

    if race in ("human", "Human"):
        for ability in ability_scores:
            ability_scores[ability] = str(int(ability_scores[ability]) + 1)
    else:
        print("Error add +1 to ability scores for being human")

    ability_bonuses = {ability: calculate_ability_bonus(score) for ability, score in ability_scores.items()}

    print("\nFinal Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"{ability}: {score} ({ability_bonuses[ability]})")

    print("Let's name your character!")
    name = input("Name: > ")

    print_character(name, size, race, level, CharClass, speed, ability_scores, language1, language2, prof, skills_proficiency)

def calculate_proficiency_bonus(level):
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



def print_character(name, size, race, level, CharClass, speed, ability_scores, language1, language2, prof, skills_proficiency):
    #Name
    print("  \n   ......................")
    print("  \n   ", name)

    if size == "5":
        print("  \n   Medium ", race)
    else:
        print("  \n   Error", race)

    print("   Level ", level, CharClass)

    print("  \n   ......................")

    #AC
    #HP
    print("   Speed ", speed, " ft.")

    print("  \n   ......................")

    print("  \n   Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"   {ability}: {score}")

    print("  \n   ......................")

    print("   Proficiencies: ")
    for skill, proficiency in skills_proficiency.items():
        if proficiency:
            print(f"{skill}: Proficient")

    print("   Languages", language1, language2)

    print("   Proficiency Bonus +", prof)

