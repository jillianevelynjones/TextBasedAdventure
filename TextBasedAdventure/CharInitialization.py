def initialize_attributes():
    ability_scores = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    initial_skills_prof = initialize_char_skills_prof()
    initial_attributes = {
        "name": False,
        "race": False,
        "class": False,
        "ability scores": ability_scores,
        "skills proficiency": initial_skills_prof
    }
    return initial_attributes

def initialize_ability_scores():
    ability_scores = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    return ability_scores

def initialize_char_skills_prof():
    char_initial_skills_proficiency_dict = {
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
    return char_initial_skills_proficiency_dict


attributes_dict = initialize_attributes()

print(attributes_dict["ability scores"])
