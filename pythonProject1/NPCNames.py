import random


class NPCNames:

    def __init__(self, race, gender):
        if race in ["dragonborn"]:
            if gender in ["female"]:
                self.first_names = ["Akra", "Aasathra", "Antrara",
                                    "Arava", "Biri", "Blendaeth",
                                    "Burana", "Chassath", "Daar",
                                    "Dentratha", "Doudra", "Driindar",
                                    "Eggren", "Farideh", "Findex",
                                    "Furrele", "Gesrethe", "Gilkass",
                                    "Harann", "Havilar", "Hethress",
                                    "Hillanot", "Jaxi", "Jezean",
                                    "Jheri", "Kadana", "Kava",
                                    "Korinn", "Megren", "Mijira",
                                    "Mishann", "Nala", "Nuthra",
                                    "Perra", "Pogranix", "Pyxrin",
                                    "Quespa", "Raiann", "Rezena",
                                    "Ruloth", "Saphara", "Savaran",
                                    "Sora", "Surina", "Synthrin",
                                    "Tatyan", "Thava", "Uadjit",
                                    "Vezera", "Zykroff"]
            elif gender in ["male"]:
                self.first_names = ["Adrex", "Arjhan", "Azzakh",
                                    "Balasar", "Baradad", "Bharash",
                                    "Bidreked", "Dadalan", "Dazzazn",
                                    "Direcris", "Donaar", "Fax",
                                    "Gargax", "Ghesh", "Gorbundus",
                                    "Greethen", "Heskan", "Hirrathak",
                                    "Ildrex", "Kaladan", "Kerkad",
                                    "Kiirith", "Kriv", "Maagog",
                                    "Medrash", "Mehen", "Mozikth",
                                    "Mreksh", "Mugrunden", "Nadarr",
                                    "Nithther", "Norkuuth", "Nykkan",
                                    "Pandjed", "Patrin", "Pijjirik",
                                    "Quarethon", "Rathkran", "Rhogar",
                                    "Rivaan", "Sethrekar", "Shamash",
                                    "Shedinn", "Srorthen", "Tarhun",
                                    "Torinn" "Trynnicus", "Valorean",
                                    "Vrondiss", "Zedaar"]
            else:
                self.first_names = ["Akra", "Aasathra", "Antrara",
                                    "Arava", "Biri", "Blendaeth",
                                    "Burana", "Chassath", "Daar",
                                    "Dentratha", "Doudra", "Driindar",
                                    "Eggren", "Farideh", "Findex",
                                    "Furrele", "Gesrethe", "Gilkass",
                                    "Harann", "Havilar", "Hethress",
                                    "Hillanot", "Jaxi", "Jezean",
                                    "Jheri", "Kadana", "Kava",
                                    "Korinn", "Megren", "Mijira",
                                    "Mishann", "Nala", "Nuthra",
                                    "Perra", "Pogranix", "Pyxrin",
                                    "Quespa", "Raiann", "Rezena",
                                    "Ruloth", "Saphara", "Savaran",
                                    "Sora", "Surina", "Synthrin",
                                    "Tatyan", "Thava", "Uadjit",
                                    "Vezera", "Zykroff", "Adrex",
                                    "Arjhan", "Azzakh", "Balasar",
                                    "Baradad", "Bharash", "Bidreked",
                                    "Dadalan", "Dazzazn", "Direcris",
                                    "Donaar", "Fax", "Gargax",
                                    "Ghesh", "Gorbundus", "Greethen",
                                    "Heskan", "Hirrathak", "Ildrex",
                                    "Kaladan", "Kerkad", "Kiirith",
                                    "Kriv", "Maagog", "Medrash",
                                    "Mehen", "Mozikth", "Mreksh",
                                    "Mugrunden", "Nadarr", "Nithther",
                                    "Norkuuth", "Nykkan", "Pandjed",
                                    "Patrin", "Pijjirik", "Quarethon",
                                    "Rathkran", "Rhogar", "Rivaan",
                                    "Sethrekar", "Shamash", "Shedinn",
                                    "Srorthen", "Tarhun", "Torinn",
                                    "Trynnicus", "Valorean", "Vrondiss", "Zedaar"]
        else:
            self.first_names = ["other"]
        self.generate_name()

    def generate_name(self):
        first_name = random.choice(self.first_names)
        return first_name