def charClass_gen(skills_proficiency):
    print("  \n   ......................")
    print("  \n   Now it's time to choose your class")
    print("   Options are: ")
    print("      Fighter")
    while True:
        CharClass = input(f"   Enter class: ")
        if CharClass in ("fighter", "Fighter"):
            class1 = "fighter"
            CharClass = Fighter(class1, skills_proficiency)
            break
        else:
            print("Sorry! Only fighter is available")
            continue
    return CharClass

def Fighter(class1, skills_proficiency):
    '''hitdice = 10
    hitpoint1 = 10 + ability_bonuses["Constitution"]
    hitpoint_max = hitpoint1
    hitpoint_increase = hitpoint_max + random.randint(1,10) + ability_bonuses["Constitution"]'''

    if class1 in ("fighter", "Fighter"):
        print("  \n   As a fighter your hit dice are 1d10")
        print("  \n   You're proficient in your choice of two of the following: ")
        print("      1. Acrobatics")
        print("      2. Animal Handling")
        print("      3. Athletics")
        print("      4. History")
        print("      5. Insight")
        print("      6. Intimidation")
        print("      7. Perception")
        chosen_skills = []
        while len(chosen_skills) < 2:
            choice = input("Skill: > ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= 7:
                    skill_name = ""
                    if choice == 1:
                        skill_name = "acrobatics"
                    elif choice == 2:
                        skill_name = "animal_handling"
                    elif choice == 3:
                        skill_name = "athletics"
                    elif choice == 4:
                        skill_name = "history"
                    elif choice == 5:
                        skill_name = "insight"
                    elif choice == 6:
                        skill_name = "intimidation"
                    elif choice == 7:
                        skill_name = "perception"

                    if skill_name not in chosen_skills:
                        chosen_skills.append(skill_name)
                        print(f"You are now proficient in {skill_name}.")
                        # Set proficiency variable to True for the chosen skill
                        globals()[f"proficiency_{skill_name.lower()}"] = True
                    else:
                        print("You have already chosen proficiency in that skill.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            else:
                print("Invalid input. Please enter a number.")
        #Proficiencies
        light_armor = True
        medium_armor = True
        heavy_armor = True
        shields = True
        simple_weapon = True
        martial_weapon = True
        STRsaveprof = True
        CONsaveprof = True
        print("You are not proficient in: ")
        for skill, proficiency in skills_proficiency.items():
            if proficiency:
                print(f"{skill}, ")