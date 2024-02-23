def character_generator():
    '''CharName = "Character 1"
    Race = input("race: ")
    charClass = input("class: ")'''

    print("   \n   ......................")
    print("  \n   We'll start with choosing Ability Scores.")
    print("  Ability score options are 15, 14, 13, 12, 10, 8.")
    print("  You must use one of each.")
    print("  Ability options are Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma")
    while True:
        STRscore = input("\n > Enter Strength score")
        print("  \n   Strength score: ", STRscore)
        if STRscore == "15":
            print("   Remaining score options: 14, 13, 12, 10, 8")
            while True:
                DEXscore = input("  \n   Enter Dexterity score")
                print("  \n   Strength Score: ", STRscore)
                print("   Dexterity Score: ", DEXscore)
                if DEXscore == "14":
                    print("  \n   Remaining score options 13, 12, 10, 8")
                    while True:
                        CONscore = input("  \n   Enter Constitution score")
                        print("  \n   Strength Score: ", STRscore)
                        print("   Dexterity Score: ", DEXscore)
                        print("   Constitution Score: ", CONscore)
                        if CONscore == "13":
                            print("  \n   Remaining score options: 12, 10, 8")






                            break
                        else:
                            print("  \n   Constituion NOT 13")
                            continue




                    break
                else:
                    print("  \n   Dexterity NOT 14")
                    continue

        else:
            print("  \n   Strength NOT 15")
            continue
        break
    '''
    print('  \n   There are two possible characters: 1 & 2')
    character_choice = input ('\n > ')

    if character_choice == '1':
        print("  \n   you chose Character 1")

    elif character_choice == '2':
        print("  \n   you chose Character 2")

    else:
        print("  \n   Oops!")

    return character_choice
    '''
