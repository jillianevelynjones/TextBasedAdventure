import ast

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

    print("\n   Ability Scores:")
    
    ability_score_dict = ast.literal_eval(attributes_dict["ability scores"])
    ability_bonus_dict = ast.literal_eval(attributes_dict["ability bonus"])
    
    for ability, score in ability_score_dict.items():
        bonus = ability_bonus_dict.get(ability, 0)
        print(f"{ability}: {score} ({bonus})")

    print("\n    ......................")
    
    print("   Languages", attributes_dict["language 1"], attributes_dict["language 2"])

    print("   Proficiency Bonus +", attributes_dict["proficiency bonus"])
