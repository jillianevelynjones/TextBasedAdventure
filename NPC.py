"""First, let's create a class called NPC
that will represent an individual NPC with various attributes"""

class NPC:
    def __init__(self,
                 race, age, gender,
                 skin_color, physical_feature, hair_color,
                 hair_length, hair_texture, facial_hair,
                 speech_patterns, personality_traits, mannerisms):
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color
        self.physical_feature = physical_feature
        self.hair_color = hair_color
        self.hair_length = hair_length
        self.hair_texture = hair_texture
        self.facial_hair = facial_hair
        self.speech_patterns = speech_patterns
        self.personality_traits = personality_traits
        self.mannerisms = mannerisms

    def __str__(self):
        return f"{self.age}-year-old {self.gender} {self.race} " \
               f"with {self.hair_length} {self.hair_texture} hair," \
               f" {self.skin_color} skin, and a {self.physical_feature}."