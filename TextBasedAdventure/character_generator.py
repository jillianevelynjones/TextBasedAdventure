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


    print("  \n   ......................")
    print("You start at level 1")
    level = 1


    print("  \n   ......................")
    print("  \n   First choose a race.")
    print("   Options are: ")
    print("      Human")
    while True:
        race = input(f"   Enter race: ").lower()
        if race in ("human", "Human"):
            print("  \n   As a human all your ability scores increase by 1")
            print("   Your size is medium")
            size = 5
            print("   Your speed is 30")
            speed = 30
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

    print("  \n   ......................")
    print("  \n   Now it's time to choose your class")
    print("   Options are: ")
    print("      Fighter")
    while True:
        charClass = input(f"   Enter class: ")
        if charClass in ("fighter", "Fighter"):
            print("stuff")
            break
        else:
            print("Sorry! Only fighter is available")
            continue


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















def print_character(size, race, level, charClass, speed, ability_scores, language1, language2, prof):
    #Name

    if size == "5":
        print("Medium ", race)
    else:
        print("Error", race)

    print("Level ", level, charClass)

    print("  \n   ......................")

    #AC
    #HP
    print("Speed ", speed, " ft.")

    print("  \n   ......................")

    print("\nAbility Scores:")
    for ability, score in ability_scores.items():
        print(f"{ability}: {score}")

    print("  \n   ......................")

    print("Languages", language1, language2)

    print("Proficiency Bonus +", prof)

