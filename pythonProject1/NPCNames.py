import random

class NPCNames:
    def __init__(self):
        self.gender = gender
        self.names_dict = {
            'human': {
                'male': ['John', 'James', 'Robert', 'William', 'Michael'],
                'female': ['Mary', 'Patricia', 'Jennifer', 'Elizabeth', 'Linda']
            },
            'elf': {
                'male': ['Legolas', 'Elrond', 'Thranduil', 'Glorfindel', 'Celeborn'],
                'female': ['Galadriel', 'Arwen', 'Tauriel', 'Nimrodel', 'Idril']
            },
            'dwarf': {
                'male': ['Gimli', 'Thorin', 'Balin', 'Dwalin', 'Fili'],
                'female': ['Dís', 'Kíli', 'Sigrid', 'Tilda', 'Glóin']
            }
        }
        self.exceptions_dict = {
            'human': ['Peter', 'Paul', 'Simon', 'Andrew', 'Matthew'],
            'elf': ['Lúthien', 'Melian', 'Aredhel', 'Elwing', 'Nessa'],
            'dwarf': ['Gudrun', 'Helga', 'Hilda', 'Sigrid', 'Thora']
        }

    def get_name(self, race):
        if race in self.names_dict:
            names = self.names_dict[race][gender]
            if names:
                return random.choice(names)
            else:
                raise ValueError(f"No {gender} names found for {race}.")
        elif race in self.exceptions_dict:
            return random.choice(self.exceptions_dict[race])
        else:
            return random.choice(self.exceptions_dict[random.choice(list(self.exceptions_dict.keys()))])
