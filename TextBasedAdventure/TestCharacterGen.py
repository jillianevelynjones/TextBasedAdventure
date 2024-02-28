import CharInitialization 
import PrintCharacter
from CharClassGen import char_class_gen
from CharRaceGen import char_race_gen

score_options = ["15", "14", "13", "12", "10", "8"]
    
class CharacterGenerator():
    
    def character_input(self, attributes_dict):

        print("\n ......................")
        print("\n First choose a race.")
        print("\n   Options are: ")
        print("     Human")
        attributes_dict["race"], self.attributes_dict = char_race_gen(attributes_dict)
        
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

        if attributes_dict["race"] in ("human", "Human"):
            print('\n   Humans get a +1 to all ability scores')
            for ability in attributes_dict["ability scores"]:
                attributes_dict["ability scores"][ability] = str(int(attributes_dict["ability scores"][ability]) + 1)
        else:
            print("Error: add +1 to ability scores for being human")
                
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

        print("\n ......................")
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
        
        attributes_dict["ability bonuses"] = {ability: calculate_ability_bonus(score) for ability, score in attributes_dict["ability scores"].items()}
        print("\n   With the ability scores you chose, your ability bonuses are: ")

        print("\n   Final Ability Scores:")
        for ability, score in attributes_dict["ability scores"].items():
            bonus = attributes_dict["ability bonuses"][ability]
            if bonus >= 0:
                print("   ", ability + ": " + str(score) + " (+" + str(bonus) + ")")
            else:
                print("   ", ability + ": " + str(score) + " (" + str(bonus) + ")")

        print("\n \n \n \n    ......................")
        
        print(type(attributes_dict["ability scores"]))
        print(type(attributes_dict["ability bonus"]))

        print("\n \n \n \n    ......................")

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
                        ability_bonus = attributes_dict["ability bonuses"].get(ability, 0)
                        proficiency_bonus = attributes_dict["proficiency bonus"]
                        skill_bonuses[skill] = ability_bonus + proficiency_bonus
                else:
                    ability = skill_ability_map.get(skill)
                    if ability:
                        ability_bonus = attributes_dict["ability bonuses"].get(ability, 0)
                        skill_bonuses[skill] = ability_bonus
        
            return skill_bonuses
        
        
        attributes_dict["skill bonus"] = calculate_skill_bonuses(attributes_dict)
        print("\n   Skill Bonuses:")
        for skill, bonus in attributes_dict["skill bonus"].items():
            print(f"      {skill}: {bonus}")
        
        print("    ......................")

        attributes_dict['AC'] = str(10 + int(attributes_dict['ability bonuses']['Dexterity']))
        attributes_dict['hit point lvl 1'] = str(10 + int(attributes_dict['ability bonuses']['Constitution']))
        attributes_dict["hit point max"] = attributes_dict["hit point lvl 1"]

        print("   Armor Class: ", attributes_dict["AC"])
        print("   Hit Points: ", attributes_dict["hit point lvl 1"])

        print(" \n \n \n \n ")

        PrintCharacter.print_character(attributes_dict)
