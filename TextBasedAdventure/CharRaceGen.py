def char_race_gen(attributes_dict):
    print("\n   ......................")
    print("\n   Now it's time to choose your race")
    print("   Options are: ")
    print("      Human")
    while True:
        char_class = input(f"   Enter race: ")
        if char_class in ("human", "Human"):
            char_race = human(attributes_dict)
            break
        else:
            print("Sorry! Only human is available")
            continue
    return char_race


def human (attributes_dict):
    print("\n   As a human all your ability scores increase by 1")
    print("\n   Your size is medium")
    attributes_dict["size"] = "5"
    print("   Your speed is 30")
    attributes_dict["speed"] = "30"
    print("   You can speak, read and write in Common and one extra language of your choice")
    attributes_dict["language 1"] = "common"
    print("\n   Your choices are: ")
    print("      Elvish")
    attributes_dict["language 2"] = input(f"   Enter language: ")
    if attributes_dict["language 2"] in ("elvish", "Elvish"):
        attributes_dict["language 2"] = "elvish"
    else:
        print("Sorry! Only language available at the time is Elvish")
        attributes_dict["language 2"] = "elvish"

    return "Human", attributes_dict
