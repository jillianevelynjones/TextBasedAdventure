"""First, let's create a class called NPC
that will represent an individual NPC with various attributes"""


class NPC:
    def __init__(self, first_name,
                 race, age, gender,
                 skin_color, hair_length, hair_color,
                 hair_texture, facial_hair, physical_feature1,
                 physical_feature2, speech_pattern1, speech_pattern2,
                 personality_trait, mannerism):
        self.first_name = first_name
        self.race = race
        self.age = age
        self.gender = gender
        self.skin_color = skin_color
        self.hair_length = hair_length
        self.hair_color = hair_color
        self.hair_texture = hair_texture
        self.facial_hair = facial_hair
        self.physical_feature1 = physical_feature1
        self.physical_feature2 = physical_feature2
        self.speech_pattern1 = speech_pattern1
        self.speech_pattern2 = speech_pattern2
        self.personality_trait = personality_trait
        self.mannerism = mannerism

    """def __str__(self):
        return f"{self.age}-year-old {self.gender} {self.race} " 
               f" {self.skin_color} skin and {self.hair_length}, {self.hair_texture}, " 
               f"{self.hair_color} hair. {self.facial_hair}. """