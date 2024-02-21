class NewNPC:
    def __init__(self, race, age, gender):
        self.race = race
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"NPC is a {self.age} year old {self.gender} {self.race}"
