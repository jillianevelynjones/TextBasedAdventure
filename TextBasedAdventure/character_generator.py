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
    print("  \n   First choose a race.")
    print("   Options are: ")
    print("      Human")
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

    print("\nFinal Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"{ability}: {score}")















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

