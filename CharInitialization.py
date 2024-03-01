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

    initial_inventory = {}
    
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
        "skill bonus": False,
        "AC": False,
        "hit point lvl 1": False,
        "hit point max": 0,
        "AC bonus": 0,
        "darkvision": False,
        "sub race": False,
        "inventory": initial_inventory
    }
    
    return initial_attributes

def initialize_skills_prof():
    weapons_and_armor_dict = weapons_and_armor()
    
    char_initial_skills_proficiency_dict = {
        "weapons and armor": weapons_and_armor_dict,
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
        "smith's tools": False,
        "brewer's tools": False,
        "mason's tools": False,
        "": False
    }
    return char_initial_skills_proficiency_dict

def weapons_and_armor():
    simple_weapons = {
        "club": False,
        "dagger": False,
        "greatclub": False,
        "handaxe": False,
        "javelin": False,
        "light hammer": False,
        "mace": False,
        "quarterstaff": False,
        "sickle": False,
        "spear": False,
        "light crossbow": False,
        "dart": False,
        "shortbow": False,
        "sling": False  
    }

    martial_weapons = {
        "battleaxe": False,
        "flail": False,
        "glaive": False,
        "greataxe": False,
        "greatsword": False,
        "halberd": False,
        "lance": False,
        "longsword": False,
        "maul": False,
        "morningstar": False,
        "pike": False,
        "rapier": False,
        "scrimitar": False,
        "shortsword": False,
        "trident": False,
        "war pick": False,
        "warhammer": False,
        "whip": False,
        "blowgun": False,
        "hand crossbow": False,
        "heavy crossbow": False,
        "longbow": False,
        "net": False
    }

    light_armor = {
        "padded": False,
        "leather": False,
        "studded leather": False
    }

    medium_armor = {
        "hide": False,
        "chain shirt": False,
        "scale mail": False,
        "breastplate": False,
        "half plate": False
    }

    heavy_armor = {
        "ring mail": False,
        "chain mail": False,
        "splint": False,
        "plate": False
    }
    
    weapons_and_armor_dict = {
        "simple weapons": simple_weapons,
        "martial weapons": martial_weapons,
        "light armor":  light_armor,
        "medium armor": medium_armor,
        "heavy armor":  heavy_armor,
        "shields": False
    }

    return weapons_and_armor_dict


attributes_dict = initialize_attributes() 
