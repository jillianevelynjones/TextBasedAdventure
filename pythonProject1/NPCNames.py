import random


class NPCNames:

    def __init__(self):
        pass

    def generate_name(self):
        first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace']
        return random.choice(first_names)
