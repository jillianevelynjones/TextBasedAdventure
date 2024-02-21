class NewNPC:
    def __init__(self, race, age, gender, skin_color, hair_length):
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color
        self.hair_length = hair_length

    def __str__(self):
        return f"NPC is a {self.age} year old {self.gender} {self.race} with {self.skin_color} and {self.hair_length}"
