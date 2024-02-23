import random


def character_generator():
    print("..........")
    print("First, choose a race.")
    print("Options are: ")
    print("Dwarf, ")
    print("Elf, ")
    print("Halfling, ")
    print("Human, ")
    print("Dragonborn, ")
    print("Gnome, ")
    print("Half-Elf, ")
    print("Half-Orc, ")
    print("and Tiefling.")
    raceDesc = input("To learn more about a race, please type their name, if not type 'choose' :\n")
    if raceDesc == "choose":
        raceChoice = input("Please choose your race: ")
    if raceDesc in ["Dwarf", "dwarf"]:
        print("..........")
        print("Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal. Though they stand well under 5 feet tall, dwarves are so broad and compact that they can weigh as much as a human standing nearly two feet taller. Their courage and endurance are also easily a match for any of the larger folk.")
        print("Your dwarf character has an assortment of inborn abilities, part and parcel of dwarven nature")
        print("Ability Score Increase. Your Constitution score increases by 2.")
        print("Age. Dwarves mature at the same rate as humans, but they’re considered young until they reach the age of 50. On average, they live about 350 years.")
        print("Size. Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium")
        print("Speed. Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.")
        print("Darkvision. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.")
        print("Dwarven Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage")
        print("Dwarven Combat Training. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.")
        print("Tool Proficiency. You gain proficiency with the artisan’s tools of your choice: smith’s tools, brewer’s supplies, or mason’s tools.")
        print("Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus")
        print("Languages. You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.")
        print("Subrace. Two main subraces of dwarves populate the worlds of D&D: hill dwarves and mountain dwarves. Choose one of these subraces.")
    else:
        print("..........")
        print("The End")

