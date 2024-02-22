class NewNPC:
    def __init__(self, race, age, gender, skin_color, hair_length, hair_texture, hair_color, facial_hair, physical_feature1):
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color
        self.hair_length = hair_length
        self.hair_texture = hair_texture
        self.hair_color = hair_color
        self.facial_hair = facial_hair
        self.physical_feature1 = physical_feature1

    def __str__(self):
        return f"NPC is age: {self.age} \n    gender: {self.gender} \n    race: {self.race} \n    skin color: {self.skin_color} \n    hair: {self.hair_length} {self.hair_texture} {self.hair_color} \n    facial hair: {self.facial_hair} \n    physical feature: {self.physical_feature1}"
