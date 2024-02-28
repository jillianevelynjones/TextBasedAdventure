def char_class_gen(attributes_dict): 

    def initialize_class_skills_prof():
        class_initial_skills_proficiency_dict = {
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
        return class_initial_skills_proficiency_dict
    
    class_skills_proficiency_dict = initialize_class_skills_prof()
    
    print("\n   ......................")
    print("\n   Now it's time to choose your class")
    print("   Options are: ")
    print("      Fighter")
    while True:
        char_class = input(f"   Enter class: ")
        if char_class in ("fighter", "Fighter"):
            char_class = fighter(class_skills_proficiency_dict, attributes_dict)
            break
        else:
            print("Sorry! Only fighter is available")
            continue
    return char_class


def fighter(class_skills_proficiency_dict, attributes_dict):
    
    print("\n   As a fighter your hit dice are 1d10")
    print("\n   ......................")
    attributes_dict["hit dice"] = 10
    
    print("\n   You are also now proficienct in all armor, shields and weapons.")
    print("   You can now add your proficiency bonus to Strength and Constitution Saving Throws.")
    
    class_skills_proficiency_dict["light armor"] = True
    class_skills_proficiency_dict["medium armor"] = True
    class_skills_proficiency_dict["heavy armor"] = True
    class_skills_proficiency_dict["shields"] = True
    class_skills_proficiency_dict["simple weapons"] = True
    class_skills_proficiency_dict["martial weapons"] = True
    class_skills_proficiency_dict["strength save"] = True
    class_skills_proficiency_dict["constitution save"] = True
    
    print("\n   ......................")
    
    print("\n   You're also proficient in your choice of two of the following: ")
    print("      1. Acrobatics")
    print("      2. Animal Handling")
    print("      3. Athletics")
    print("      4. History")
    print("      5. Insight")
    print("      6. Intimidation")
    print("      7. Perception")

    chosen_skills = []
    temp_skill = ""
    while len(chosen_skills) < 2:
        choice = input("Skill: > ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 7:
                if choice == 1:
                    temp_skill = "acrobatics"
                elif choice == 2:
                    temp_skill = "animal handling"
                elif choice == 3:
                    temp_skill = "athletics"
                elif choice == 4:
                    temp_skill = "history"
                elif choice == 5:
                    temp_skill = "insight"
                elif choice == 6:
                    temp_skill = "intimidation"
                elif choice == 7:
                    temp_skill = "perception"

                if not class_skills_proficiency_dict[temp_skill]:
                    class_skills_proficiency_dict[temp_skill] = True
                    chosen_skills.append(temp_skill)
                    print(f"You are now proficient in {temp_skill}.")
                else:
                    print("  You have already chosen proficiency in that skill.")
            else:
                print("   Invalid choice. Please enter a number between 1 and 7.")
        else:
            print("   Invalid input. Please enter a number.")

    print("\n   ......................")
    print("\n   Now it's time to choose your fighting style")
    print("   Options are: ")
    print("      Defense")
    while True:
        char_class = input(f"   Enter fighting style: ")
        if char_class in ("defense", "Defense"):
            # AC SHIT
            break
        else:
            print("Sorry! Only defense is available")
            continue

    return "Fighter", class_skills_proficiency_dict, attributes_dict
