def initialize_attributes():
    ability_scores = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }
    initial_skills_prof = initialize_skills_prof()
    initial_attributes = {
        "name": False,
        "race": False,
        "size": False,
        "speed": False,
        "language 1": False,
        "language 2": False,
        "class": False,
        "hit dice": False,
        "skills proficiency": initial_skills_prof,
        "sub class": False,
        "ability scores": ability_scores,
        "proficiency bonus": False,
        "ability bonus": False,
        "skill bonus": False
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

def initialize_skills_prof():
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

