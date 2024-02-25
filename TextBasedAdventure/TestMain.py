import TestCharacterGen
from TestCharacterGen import print_character
import time
import pickle
import sys


# miscellaneous functions + procedures

def w(t):
    time.sleep(t)

def version_counter(filename="adventure_colussus_version_counter.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


counter = version_counter()


def t(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.021)


# Define the save_character function
def save_character(save_name, character_sheet):
    save_name_pickle = save_name + '.pickle'
    print('> saving character')
    try:
        with open(save_name_pickle, 'wb') as f:  # Open in binary mode ('wb') for pickle
            pickle.dump(character_sheet, f)  # Serialize and write the character sheet object
        print('> character saved successfully')
    except Exception as e:
        print('> error saving character:', e)

# Define the function to check the pickle file
def check_pickle_file(file_path):
    try:
        print("Attempting to open file:", file_path)
        with open(file_path, 'rb') as f:
            character_sheet = pickle.load(f)
            print("File is a valid pickle file.")
            print("Contents:")
            print_character(character_sheet)
    except Exception as e:
        print("Error loading pickle file:", e)

# main game
def main():

    character_generator = TestCharacterGen.CharacterGenerator()
    print(character_generator)
    attributes_dict = {}
    character_generator.initialize_attributes()

    while True:
        print('\n  <Saga of the Infected>')
        w(0.5)
        print('\n > [1] create new game')
        print(' > [2] load existing game')
        print(' > [3] end game')
        choice = input("\n > ")

        if choice == '1':
            t("\n > you have chosen to create a new game: ")
            print("\n   ......................")
            print('\n   we will begin with creating your character: ')

            attributes_dict = character_generator.get_attributes(attributes_dict)
            print(attributes_dict)

            print("\n   pick a file name to save under")
            character_file_name = input('> ')
            pickle_file_path = character_file_name + ".pickle"
            check_pickle_file(pickle_file_path)

            character_sheet = TestCharacterGen.print_character(attributes_dict)
            save_character(character_file_name, character_sheet)
            print("\n   game saved as: ", character_file_name)

            break

        elif choice == '2':
            t("\n > you have chosen to load an existing game: ")
            print('  \n  we will begin with choosing an existing character:')
            character_file_name = input('\n > character file name: ')
            print(load_character(character_file_name))

            break

        elif choice == '3':
            t(' > Goodbye!')
            sys.exit()
            break

        else:
            t('incorrect response. please try again')
            continue

if __name__ == "__main__":
    main()

# Ask the user for the file name
character_file_name = input("Enter the name of the pickle file (without extension): ")

# Create the file path by appending the file name with '.pickle' extension
pickle_file_path = character_file_name + ".pickle"

# Call the function to check the pickle file
check_pickle_file(pickle_file_path)

def load_character(load_name):
    load_name_pickle = load_name + '.pickle'
    print(' > Loading character from:', load_name_pickle)  # Debug statement
    t(' > loading character...')
    w(1)
    try:
        with open(load_name_pickle, "rb") as pickle_in:  # Open in binary mode ('rb')
            character_sheet = pickle.load(pickle_in)
        if character_sheet is None:
            raise ValueError("Loaded character sheet is None")
        t(' > character loaded successfully\n')
        t('\n> welcome back ')
        w(0.5)
        t('\n> here\'s the character you chose last time \n')
        print(' >', character_sheet)
        return character_sheet
    except FileNotFoundError:
        t(' > character file not found\n')
        return False
    except Exception as e:
        print(' > Error loading character:', e)  # Debug statement
        return False