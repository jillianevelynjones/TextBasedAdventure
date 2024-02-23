import random


def character_generator():
    print('  \n   There are two possible characters: 1 & 2')
    character_choice = input ('\n > ')

    if character_choice == '1':
        print("  \n   you chose Character 1")

    elif character_choice == '2':
        print("  \n   you chose Character 2")

    else:
        print("  \n   Oops!")