import CharInitialization 
import PrintCharacter
import Dice
from CharClassGen import char_class_gen
from CharRaceGen import char_race_gen

score_options = ["15", "14", "13", "12", "10", "8"]
    
class CharacterGenerator():
    
    def character_input(self, attributes_dict):

        attributes_dict["race"], attributes_dict["skills proficiency"], self.attributes_dict = char_race_gen(attributes_dict)
        
        attributes_dict["class"], attributes_dict["skills proficiency"], self.attributes_dict = char_class_gen(attributes_dict)

        print("    ......................")
        print("\n  Now we'll choose Ability Scores.")
        print("  Ability score options are 15, 14, 13, 12, 10, 8.")
        print("  You must use one of each.")
        print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")

        ability_scores = attributes_dict["ability scores"]
        
        for ability in ability_scores:
            print("\n   Choose " + ability + " score:")
            while True:
                score = input("   Enter " + ability + " score: ")
                if score in score_options:
                    attributes_dict["ability scores"][ability] = score
                    score_options.remove(score)
                    print("\n   Remaining score options: " + ', '.join(score_options))
                    break
                else:
                    print("\n   Invalid " + ability + " score. Please choose from " + ', '.join(score_options))

        print("\n \n \n \n ", attributes_dict["race"], attributes_dict["sub race"])
        
        if attributes_dict["race"] == "human":
            for ability in attributes_dict["ability scores"]:
                attributes_dict["ability scores"][ability] = str(int(attributes_dict["ability scores"][ability]) + 1)
        elif attributes_dict["race"] == "dwarf":
            attributes_dict["ability scores"]["Constitution"] = str(int(attributes_dict["ability scores"]["Constitution"]) + 2)
            if attributes_dict["sub race"] == "hill dwarf":
                attributes_dict["ability scores"]["Wisdom"] = str(int(attributes_dict["ability scores"]["Wisdom"]) + 1)
            elif attributes_dict["sub race"] == "mountain dwarf":
                attributes_dict["ability scores"]["Strength"] = str(int(attributes_dict["ability scores"]["Strength"]) + 2)
        else:
            print("Error: add racial bonus to ability score")
                
        print("\n   Final Ability Scores:")
        for ability, score in attributes_dict["ability scores"].items():
            print("   ", ability + ": " + str(score))

        
        print("    ......................")
        print("\n Let's name your character!")
        attributes_dict['name'] = input("   Name: > ")

        self.name = attributes_dict["name"]
        self.race = attributes_dict["race"]
        self.char_class = attributes_dict["class"]
        self.ability_scores = attributes_dict["ability scores"]
        self.chargen_skills_proficiency_dict = attributes_dict["skills proficiency"]


        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "ability scores": self.ability_scores,
            "skills proficiency": self.chargen_skills_proficiency_dict
        }
        

    def attribute_calc(self, attributes_dict):

        def calculate_proficiency_bonus():
            if 1 <= attributes_dict["level"] <= 4:
                return 2
            elif 5 <= attributes_dict["level"] <= 8:
                return 3
            elif 9 <= attributes_dict["level"] <= 12:
                return 4
            elif 13 <= attributes_dict["level"] <= 16:
                return 5
            elif 17 <= attributes_dict["level"] <= 20:
                return 6
            else:
                return None

        print("\n   ......................")
        print("\n   You start at level 1")
        attributes_dict["level"] = 1

        attributes_dict["proficiency bonus"] = calculate_proficiency_bonus()
        print("   That makes your proficiency bonus ", attributes_dict["proficiency bonus"])

        print("\n    ......................")
                        
        def calculate_ability_bonus(score):
            if score == "20":
                return 5
            elif score in ["18", "19"]:
                return 4
            elif score in ["16", "17"]:
                return 3
            elif score in ["14", "15"]:
                return 2
            elif score in ["12", "13"]:
                return 1
            elif score in ["10", "11"]:
                return 0
            elif score in ["8", "9"]:
                return -1
            elif score in ["6", "7"]:
                return -2
            elif score in ["4", "5"]:
                return -3
            elif score in ["2", "3"]:
                return -4
            elif score == "1":
                return -5
            else:
                return None
        
        attributes_dict["ability bonus"] = {ability: calculate_ability_bonus(score) for ability, score in attributes_dict["ability scores"].items()}
        print("\n   With the ability scores you chose, your ability bonuses are: ")

        print("\n   Final Ability Scores:")
        for ability, score in attributes_dict["ability scores"].items():
            bonus = attributes_dict["ability bonus"][ability]
            if bonus >= 0:
                print("   ", ability + ": " + str(score) + " (+" + str(bonus) + ")")
            else:
                print("   ", ability + ": " + str(score) + " (" + str(bonus) + ")")

        print("    ......................")

        def calculate_skill_bonuses(attributes_dict):
            skill_ability_map = {
                "athletics": "Strength",
                "acrobatics": "Dexterity",
                "sleight of hand": "Dexterity",
                "stealth": "Dexterity",
                "arcana": "Intelligence",
                "history": "Intelligence",
                "investigation": "Intelligence",
                "nature": "Intelligence",
                "religion": "Intelligence",
                "animal handling": "Wisdom",
                "insight": "Wisdom",
                "medicine": "Wisdom",
                "perception": "Wisdom",
                "survival": "Wisdom",
                "deception": "Charisma",
                "intimidation": "Charisma",
                "performance": "Charisma",
                "persuasion": "Charisma"
            }
        
            skill_bonuses = {}
        
            for skill, proficiency in attributes_dict["skills proficiency"].items():
                if proficiency:
                    ability = skill_ability_map.get(skill)
                    if ability:
                        ability_bonus = attributes_dict["ability bonus"].get(ability, 0)
                        proficiency_bonus = attributes_dict["proficiency bonus"]
                        skill_bonuses[skill] = ability_bonus + proficiency_bonus
                else:
                    ability = skill_ability_map.get(skill)
                    if ability:
                        ability_bonus = attributes_dict["ability bonus"].get(ability, 0)
                        skill_bonuses[skill] = ability_bonus
        
            return skill_bonuses
        
        
        attributes_dict["skill bonus"] = calculate_skill_bonuses(attributes_dict)
        print("\n   Skill Bonuses:")
        for skill, bonus in attributes_dict["skill bonus"].items():
            print(f"      {skill}: {bonus}")
        
        print("    ......................")

        attributes_dict['AC'] = str(10 + int(attributes_dict['ability bonus']['Dexterity']) + int(attributes_dict["AC bonus"]))
        attributes_dict['hit point lvl 1'] = 10 + int(attributes_dict['ability bonus']['Constitution'])
        attributes_dict["hit point max"] = attributes_dict["hit point max"] + attributes_dict["hit point lvl 1"]

        print("   Armor Class: ", attributes_dict["AC"])
        print("   Hit Points: ", attributes_dict["hit point lvl 1"])

        print(" \n \n \n \n ")

        PrintCharacter.print_character(attributes_dict)

    def starting_equipment(self, attributes_dict):
        if attributes_dict["class"] == "fighter":
            attributes_dict["gp"] = Dice.d4(5)*10
            print("You start out with ", attributes_dict["gp"], " gp")
        
        return attributes_dict
        
