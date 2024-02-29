from Character_Generator import CharacterGenerator
import CharInitialization
import PrintCharacter
import time
import sys
import json


def w(t):
    time.sleep(t)


def t(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)


import json

def save_character(save_name, attributes_dict):
    save_name_json = save_name + '.json'
    print('> saving character')
    try:
        with open(save_name_json, 'w') as f:
            json.dump(attributes_dict, f, indent=4)
        print('> character saved successfully')
    except Exception as e:
        print('> error saving character:', e)


def load_character(load_name):
    load_name_json = load_name + '.json'
    print('\n > Loading character from:', load_name_json)
    t(' > loading character...')
    w(1)
    try:
        with open(load_name_json, "r") as f:
            attributes_dict = json.load(f)
            print("\n > Character loaded successfully.")
            return attributes_dict
    except FileNotFoundError:
        t('\n > character file not found\n')
        return False
    except Exception as e:
        print('\n > Error loading character:', e)
        return False


def main():

    # Opening Menu
    while True:
        print('\n  <Saga of the Infected>')
        w(0.5)
        print('\n > [1] create new game')
        print(' > [2] load existing game')
        print(' > [3] end game')
        choice = input("\n > ")

        if choice == '1':
            print("\n > You have chosen to create a new game:")
            print("\n   ......................")
            print('\n   We will begin with creating your character: ')

            attributes_dict = CharInitialization.attributes_dict
            character_generator = CharacterGenerator()
            character_generator.character_input(attributes_dict)
            character_generator.attribute_calc(attributes_dict)
            character_generator.starting_equipment(attributes_dict)

            print("\n   Pick a file name to save under:")
            character_file_name = input('> ')

            save_character(character_file_name, attributes_dict)
            print("\n   Game saved as:", character_file_name)

            break

        elif choice == '2':
            t("\n > you have chosen to load an existing game: ")
            print('  \n  we will begin with choosing an existing character:')
            character_file_name = input('\n > character file name: ')

            attributes_loaded = load_character(character_file_name)
            PrintCharacter.print_character(attributes_loaded)

            break

        elif choice == '3':
            t(' > Goodbye!')
            sys.exit()
            # break

        else:
            t('incorrect response. please try again')
            continue


if __name__ == "__main__":
    main()
