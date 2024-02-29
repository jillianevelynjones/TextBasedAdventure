import CharInitialization


def char_class_gen(attributes_dict): 
    
    class_skills_proficiency_dict = CharInitialization.initialize_skills_prof()
    
    print("\n   ......................")
    print("\n   Now it's time to choose your class")
    print("   Options are: ")
    print("      Fighter")
    while True:
        char_class = input(f"\n   Enter class: ")
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
    
    weapons_and_armor_dict = class_skills_proficiency_dict.get("weapons and armor", {})
    for weapon in weapons_and_armor_dict["martial weapons"]:
        weapons_and_armor_dict["martial weapons"][weapon] = True
    for weapon in weapons_and_armor_dict["simple weapons"]:         weapons_and_armor_dict["simple weapons"][weapon] = True
    for armor in weapons_and_armor_dict["light armor"]:
        weapons_and_armor_dict["light armor"][armor] = True
    for armor in weapons_and_armor_dict["medium armor"]:
        weapons_and_armor_dict["medium armor"][armor] = True
    for armor in weapons_and_armor_dict["heavy armor"]:
        weapons_and_armor_dict["heavy armor"][armor] = True
    weapons_and_armor_dict["shields"] = True
    
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
        choice = input("\n   Skill: > ")
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
    print("      Defense (+1 bonus to AC)")
    while True:
        attributes_dict["sub class"] = input(f"\n   Enter fighting style: ")
        if attributes_dict["sub class"] in ("defense", "Defense"):
            attributes_dict["AC bonus"] = 1
            break
        else:
            print("Sorry! Only defense is available")
            continue

    return "Fighter", class_skills_proficiency_dict, attributes_dict
