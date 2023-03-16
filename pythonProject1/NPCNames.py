import random


class NPCNames:

    def __init__(self, race):
        match race:
            case "human":
                self.first_names = ["John", "Emily", "Michael", "Samantha"]
            case _:
                self.first_names = ["Legolas", "Arwen", "Elrond", "Galadriel"]

        self.generate_name()

    def generate_name(self):
        first_name = random.choice(self.first_names)
        return first_name
