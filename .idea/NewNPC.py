class NewNPC:
    def __init__(self, race, age, gender, skin_color, hair_length, hair_texture, hair_color, facial_hair):
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color
        self.hair_length = hair_length
        self.hair_texture = hair_texture
        self.hair_color = hair_color
        self.facial_hair = facial_hair

    def __str__(self):
        return f"NPC is age: {self.age} gender: {self.gender} race: {self.race} skin color: {self.skin_color} hair: {self.hair_length} {self.hair_texture} {self.hair_color} facial hair: {self.facial_hair}"
