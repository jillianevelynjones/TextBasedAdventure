
def char_class_gen(skills_proficiency_dict):
  print("  \n   ......................")
  print("  \n   Now it's time to choose your class")
  print("   Options are: ")
  print("      Fighter")
  while True:
    char_class = input(f"   Enter class: ")
    if char_class in ("fighter", "Fighter"):
      class1 = "Fighter"
      char_class = fighter(skills_proficiency_dict)
      break
    else:
      print("Sorry! Only fighter is available")
      continue
  return char_class

def fighter(skills_proficiency_dict):
  print("  \n   As a fighter your hit dice are 1d10")
  print("  \n   ......................")

  skills_proficiency_dict["light armor"] = True
  skills_proficiency_dict["medium armor"] = True
  skills_proficiency_dict["heavy armor"] = True
  skills_proficiency_dict["shields"] = True
  skills_proficiency_dict["simple weapons"] = True
  skills_proficiency_dict["martial weapons"] = True
  skills_proficiency_dict["strength save"] = True
  skills_proficiency_dict["constitution save"] = True

  print("  \n   You're also proficient in your choice of two of the following: ")
  print("      1. Acrobatics")
  print("      2. Animal Handling")
  print("      3. Athletics")
  print("      4. History")
  print("      5. Insight")
  print("      6. Intimidation")
  print("      7. Perception")

  chosen_skills = []
  temp_skill = ""
  while len(chosen_skills) < 2:
    choice = input("Skill: > ")
    if choice.isdigit():
      choice = int(choice)
      if 1 <= choice <= 7:
        if choice == 1:
          temp_skill = "acrobatics"
        elif choice == 2:
          temp_skill = "animal handling"
        elif choice == 3:
          temp_skill = "athletics"
        elif choice == 4:
          temp_skill = "history"
        elif choice == 5:
          temp_skill = "insight"
        elif choice == 6:
          temp_skill = "intimidation"
        elif choice == 7:
          temp_skill = "perception"

        if not skills_proficiency_dict[temp_skill]:
          skills_proficiency_dict[temp_skill] = True
          chosen_skills.append[temp_skill]
          print(f"You are now proficient in {temp_skill}.")
        else:
          print("You have already chosen proficiency in that skill.")
      else:
        print("Invalid choice. Please enter a number between 1 and 7.")
    else:
      print("Invalid input. Please enter a number.")

  print("  \n   ......................")
  print("  \n   Now it's time to choose your fighting style")
  print("   Options are: ")
  print("      Defense")
  while True:
    char_class = input(f"   Enter fighting style: ")
    if char_class in ("defense", "Defense"):
      # AC SHIT
      break
    else:
      print("Sorry! Only defense is available")
      continue

  return "Fighter"
