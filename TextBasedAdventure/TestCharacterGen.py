



def print_character(attributes_dict):
  attributes = attributes_dict

  # Name
  print("  \n   ......................")
  print("  \n   ", attributes["name"])

  if attributes["size"] == "5":
    print("  \n   Medium ", attributes["race"])
  else:
    print("  \n   Error", attributes["race"])

  print("  \n   ......................")


def save_character(save_name, character_sheet):
  save_name_pickle = save_name + '.pickle'
  print('> saving character')
  try:
    with open(save_name_pickle, 'w') as f:
      f.write(character_sheet)  # Write the character sheet string to the file
    print('> character saved successfully')
  except Exception as e:
    print('> error saving character:', e)



class CharacterGenerator:
  def __init__(self):
    self.name = False
    self.size = False
    self.race = False
    self.level = False
    self.AC = False
    self.hitdice = False
    self.hitpoint = False
    self.hitpoint_max = False
    self.char_class = False
    self.speed = False
    self.ability_scores = False
    self.language1 = False
    self.language2 = False
    self.prof = False
    self.skills_proficiency = False
    self.attributes_dict = {}

  def initialize_attributes(self):
    self.name = None
    self.size = None
    self.race = None
    self.level = None
    self.AC = None
    self.hitdice = None
    self.hitpoint = None
    self.hitpoint_max = None
    self.char_class = None
    self.speed = None
    self.ability_scores = None
    self.language1 = None
    self.language2 = None
    self.prof = None
    self.skills_proficiency = None

  def get_attributes(self, attributes_dict):
    attributes = attributes_dict
    print("\n ......................")
    print("\n You start at level 1")
    attributes["level"] = 1

    print("\n ......................")
    print("\n First choose a race.")
    print("\n   Options are: ")
    print("     Human")
    while True:
      attributes["race"] = input(f"\n   Enter race: ").lower()
      if attributes["race"] in ("human", "Human"):
    # print("\n   As a human all your ability scores increase by 1")
        print("\n Your size is medium")
        attributes["size"] = "5"
        break
      else:
        print("Sorry! Only human is available")
        continue

    print("\n Let's name your character!")
    attributes['name'] = input("   Name: > ")  # Corrected syntax

    self.name = attributes["name"]
    self.size = attributes["size"]
    self.race = attributes["race"]  # Assign race to self.race

    print_character(attributes)

    return {
        "name": self.name,
        "size": self.size,
        "race": self.race,  # Include race in the returned dictionary
        "level": self.level
    }
