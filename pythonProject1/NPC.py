"""First, let's create a class called NPC
that will represent an individual NPC with various attributes"""


class NPC:
    def __init__(self,
                 race, age, gender,
                 skin_color):
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color

    def __str__(self):
        return f"{self.age}-year-old {self.gender} {self.race} " \
               f" {self.skin_color} skin."
