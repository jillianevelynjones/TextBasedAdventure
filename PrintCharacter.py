from Inventory import Inventory_Class



def print_character(attributes_dict):

    print("  \n  ......................")
    print("  \n  ", attributes_dict["name"])

    if attributes_dict["size"] == "5":
        print("  \n   Medium ", attributes_dict["race"])
    else:
        print("  \n  Error", attributes_dict["race"])

    print("   Level ", attributes_dict["level"], attributes_dict["sub class"], attributes_dict["class"])

    print("  \n  ......................")

    print("  \n  Armor Class ", attributes_dict["AC"])
    print("  \n  Hit Point Max ", attributes_dict["hit point max"], " (", attributes_dict["level"], "d", attributes_dict["hit dice"], ")")
    print("  \n  Speed ", attributes_dict["speed"], " ft.")

    print("  \n  ......................")

    print("\n   Ability Scores: ")
    for ability, score in attributes_dict["ability scores"].items():
        bonus = attributes_dict["ability bonus"][ability]
        if bonus >= 0:
            print("   ", ability + ": " + str(score) + " (+" + str(bonus) + ")")
        else:
            print("   ", ability + ": " + str(score) + " (" + str(bonus) + ")")

    print("\n    ......................")
    
    print("   Languages", attributes_dict["language 1"], ", ", attributes_dict["language 2"])

    print("   Proficient Skills: ")
    for skill, bonus in attributes_dict["skill bonus"].items():
        if attributes_dict["skills proficiency"].get(skill, True):
            if bonus >= 0:
                print(f"      {skill} +{bonus}, ")
            else:
                print(f"      {skill} {bonus}, ")

    print("\n    ......................")

    inventory = Inventory_Class(attributes_dict)
    attributes_dict["inventory"] = inventory.get_inventory()
    print(inventory.display_inventory())
