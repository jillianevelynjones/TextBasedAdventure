import CharInitialization 
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

        print("\n \n SKILL PROF BEFORE CLASS", attributes_dict["skills proficiency"])
        
        attributes_dict["class"], attributes_dict["skills proficiency"], self.attributes_dict = char_class_gen(attributes_dict)

        print("SKILL PROF AFTER CLASS", attributes_dict["skills proficiency"])

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
