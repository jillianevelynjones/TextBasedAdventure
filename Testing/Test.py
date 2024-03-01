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
