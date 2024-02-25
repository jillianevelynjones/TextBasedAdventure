def char_class_gen(skills_proficiency):
  print("  \n   ......................")
  print("  \n   Now it's time to choose your class")
  print("   Options are: ")
  print("      Fighter")
  while True:
    char_class = input(f"   Enter class: ")
    if char_class in ("fighter", "Fighter"):
      class1 = "Fighter"
      char_class = fighter(skills_proficiency)
      break
    else:
      print("Sorry! Only fighter is available")
      continue
  return char_class


def fighter(skills_proficiency):
  print("  \n   As a fighter your hit dice are 1d10")
  print("  \n   ......................")

  skills_proficiency["light armor"] = True
  skills_proficiency["medium armor"] = True
  skills_proficiency["heavy armor"] = True
  skills_proficiency["shields"] = True
  skills_proficiency["simple weapons"] = True
  skills_proficiency["martial weapons"] = True
  skills_proficiency["strength save"] = True
  skills_proficiency["constitution save"] = True

  print("  \n   You're also proficient in your choice of two of the following: ")
  print("      1. Acrobatics")
  print("      2. Animal Handling")
  print("      3. Athletics")
  print("      4. History")
  print("      5. Insight")
  print("      6. Intimidation")
  print("      7. Perception")
  chosen_skills = []
  while len(chosen_skills) < 2:
    choice = input("Skill: > ")
    if choice.isdigit():
      choice = int(choice)
      if 1 <= choice <= 7:
        skill_name = ""
        if choice == 1:
          skill_name = "acrobatics"
        elif choice == 2:
          skill_name = "animal handling"
        elif choice == 3:
          skill_name = "athletics"
        elif choice == 4:
          skill_name = "history"
        elif choice == 5:
          skill_name = "insight"
        elif choice == 6:
          skill_name = "intimidation"
        elif choice == 7:
          skill_name = "perception"

        if not skills_proficiency[skill_name]:
          skills_proficiency[skill_name] = True
          chosen_skills.append(skill_name)
          print(f"You are now proficient in {skill_name}.")
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
