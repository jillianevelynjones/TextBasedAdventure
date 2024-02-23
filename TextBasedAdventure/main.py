from character_generator import character_generator
from os import system
import time
import datetime
import pickle
import sys


#miscellaneous functions + procedures

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

def save_character(save_name, character):
    save_name_pickle = save_name + '.pickle'
    t('> saving character')
    w(1)
    with open(save_name_pickle, 'wb') as f:
        pickle.dump(character, f)
        t('> character saved successfully')

def load_character(load_name):
    load_name_pickle = load_name + '.pickle'
    t(' > loading character...')
    w(1)
    pickle_in = open(load_name_pickle,"rb")
    character = pickle.load(pickle_in)
    t(' > character loaded successfully\n')
    t('\n> welcome back ')
    t(character['name'])
    t('!!!\n')
    w(0.5)
    t('\n> here are your stats from last time: \n')
    print(' >',character)


# main game

w(0.5)
e = datetime.datetime.now()
print('\n  <Saga of the Infected>         version: v', counter, '| current date: ', e)
w(0.5)
print('\n > [1] create new game')
print(' > [2] load existing game')
print(' > [3] end game')
print(' > [4] credits')
choice = input("\n > ")

if choice == '1':

    t("\n > you have chosen to create a new game: redirecting...")
    w(0.75)
    system('cls')
    print('  \n   we will begin with creating your character: ')
    w(0.5)
    w(0.3)

    character_generator()




elif choice == '2':

    t("\n > you have chosen to load an existing game: redirecting...")
    w(0.75)
    system('cls')
    w(0.5)
    print(
        '  \n  we will begin with choosing an existing character:                             quick tip: make sure it exists!')
    w(0.5)

    character_file_name = input('\n > character file name: ')
    load_character(character_file_name)



elif choice == '3':

    t(' > ending session...')
    w(0.5)
    t(' > session ended successfully')
    w(1)
    sys.exit()

elif choice == '4':
    pass

else:
    t('incorrect response. please try again')