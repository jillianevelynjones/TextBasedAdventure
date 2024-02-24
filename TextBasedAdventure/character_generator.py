def character_generator():
    ability_scores = {
        "Strength": None,
        "Dexterity": None,
        "Constitution": None,
        "Intelligence": None,
        "Wisdom": None,
        "Charisma": None
    }

    score_options = ["15", "14", "13", "12", "10", "8"]

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

    print("\nFinal Ability Scores:")
    for ability, score in ability_scores.items():
        print(f"{ability}: {score}")
