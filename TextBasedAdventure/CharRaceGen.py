import CharInitialization

def char_race_gen(attributes_dict):
    
    race_skills_proficiency_dict = CharInitialization.initialize_skills_prof()
    
    print("\n ......................")
    print("\n First choose a race.")
    print("\n   Options are: ")
    print("     Human")
    print("     Dwarf")
    while True:
        char_class = input(f"\n   Enter race: ")
        if char_class in ("human", "Human"):
            char_race = human(race_skills_proficiency_dict, attributes_dict)
            break
        elif char_class in ("dwarf", "Dwarf"):
            char_race = dwarf(race_skills_proficiency_dict, attributes_dict)
            break
        else:
            print("Sorry! Only human is available")
            continue
    return char_race


def human (race_skills_proficiency_dict, attributes_dict):
    print("\n   As a human all your ability scores increase by 1")
    print("   Your size is medium")
    attributes_dict["size"] = "5"
    print("   Your speed is 30")
    attributes_dict["speed"] = "30"
    print("   You can speak, read and write in Common and one extra language of your choice")
    attributes_dict["language 1"] = "common"
    print("   Your choices are: ")
    print("      Elvish")
    attributes_dict["language 2"] = input(f"\n   Enter language: ")
    if attributes_dict["language 2"] in ("elvish", "Elvish"):
        attributes_dict["language 2"] = "elvish"
    else:
        print("Sorry! Only language available at the time is Elvish")
        attributes_dict["language 2"] = "elvish"

    return "Human", race_skills_proficiency_dict, attributes_dict


def dwarf (race_skills_proficiency_dict, attributes_dict):
    print("\n   As a dwarf your constitution score increases by 2")
    print("   Your size is medium")
    attributes_dict["size"] = "5"
    print("   Your speedis 25.") 
    attributes_dict["speed"] = "30"
    print("   You have dark vision")
    attributes_dict["dark vision"] = "60"
    print("   You have advantage on saving throws against poison,and you have resistance against poison damage") #How do I code that?
    
    weapons_and_armor_dict = race_skills_proficiency_dict.get("weapons and armor", {})
    
    print("\n   You now have proficiency with the battleaxe, handaxe, light hammer, and warhammer")
    if "martial weapons" in weapons_and_armor_dict:
        weapons_and_armor_dict["martial weapons"]["battleaxe"] = True
        weapons_and_armor_dict["simple weapons"]["handaxe"] = True
        weapons_and_armor_dict["simple weapons"]["light hammer"] = True
        weapons_and_armor_dict["martial weapons"]["warhammer"] = True
    else:
        print("Error: 'martial weapons' not found in weapons_and_armor_dict")

    race_skills_proficiency_dict["weapons and armor"] = weapons_and_armor_dict


    print("\n   ......................")
    
    print("\n   You're also proficient in the artisan's tools of your choice ")
    print("      1. Smith's Tools")
    print("      2. Brewer's Supplies")
    print("      3. Mason's Tools")

    temp_skill = ""
    choice = input("\n   Skill: > ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 7:
            if choice == 1:
                temp_skill = "smith's tools"
            elif choice == 2:
                temp_skill = "brewer's supplies"
            elif choice == 3:
                temp_skill = "mason's tools"
            else:
                print("   Invalid choice. Please enter a number between 1 and 3.")
            race_skills_proficiency_dict[temp_skill] = True
            print(f"You are now proficient in {temp_skill}.")
        else:
            print("   Invalid input. Please enter a number.")

    print("You can speak, read and write Common and Dwarvish.")
    attributes_dict["language 1"] = "common"
    attributes_dict["language 2"] = "dwarvish"

    print("\n   ......................")
    print("\n   You have your choice between two subraces: ")
    print("      1. Hill Dwarf")
    print("      2. Mountain Dwarf")
    while True:
        sub_race_choice = input("\n   Enter subrace: ")
        if sub_race_choice == "1":
            print("You have chosen hill dwarf.")
            attributes_dict["sub race"] = "hill dwarf"
            print("Your wisdom score increases by 1 and your hit point maximum increases by 1, and it increases by 1 every time you gain a level.")
            attributes_dict["ability scores"]["Wisdom"] = int(attributes_dict["ability scores"]["Wisdom"]) + 1
            attributes_dict["hit point max"] = int(attributes_dict["hit point max"]) + 1
            break
        elif sub_race_choice == "2":
            print("You have chosen mountain dwarf")
            attributes_dict["sub race"] = "mountain dwarf"
            print("Your strength score increases by 2 and you have proficiency with light and medium armor.")
            attributes_dict["ability scores"]["Strength"] = int(attributes_dict["ability scores"]["Strength"]) + 2
            for armor in weapons_and_armor_dict["light armor"]:
                weapons_and_armor_dict["light armor"][weapon] = True
            for armor in weapons_and_armor_dict["medium armor"]:
                weapons_and_armor_dict["medium armor"][armor] = True
            break
        else:
            print("Invalid choice. Please enter either 1 or 2") 
            continue 
    
    return "Dwarf", race_skills_proficiency_dict, attributes_dict
