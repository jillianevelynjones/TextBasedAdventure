import random


class HumanNames:

    def __init__(self, skin_color, gender):
        if skin_color in ["reddish brown sepia"]:
            if gender in ["female"]:
                self.human_names = ["Ahuiliztli", "Atl", "Centehua",
                                    "Chalchiuitl", "Chipahua", "Cihuaton",
                                    "Citlali", "Citlalmina", "Coszcatl",
                                    "Cozamalotl", "Cuicatl", "Eleuia",
                                    "Eloxochitl", "Eztli", "Ichtaca",
                                    "Icnoyotl", "Ihuicatl", "Ilhuitl",
                                    "Itotia", "Iuitl", "Ixcatzin",
                                    "Izel", "Malinalxochitl", "Mecatl",
                                    "Meztli", "Miyaoaxochitl", "Mizquixaual",
                                    "Moyolehuani", "Nahuatl", "Necahual",
                                    "Nenetl", "Nochtli", "Noxochicoztli",
                                    "Ohtli", "Papan", "Patli",
                                    "Quetzalxochitl", "Sacnite", "Teicui",
                                    "Tepin", "Teuicui", "Teyacapan",
                                    "Tlaco", "Tlacoehua", "Tlacotl",
                                    "Tlalli", "Tlanextli", "Xihuitl",
                                    "Xiuhcoatl", "Xiuhtonal"]
            elif gender in ["male"]:
                self.human_names = ["Achcauhtli", "Amoxtli", "Chicahua",
                                    "Chimalli", "Cipactli", "Coaxoch",
                                    "Coyotl", "Cualli", "Cuauhtémoc",
                                    "Cuetlachtilo", "Cuetzpalli", "Cuixtli",
                                    "Ehecatl", "Etalpalli", "Huemac",
                                    "Huitzilihuitl", "Iccauhtli", "Ilhicamina",
                                    "Itztli", "Ixtli", "Mahuizoh",
                                    "Manauia", "Matlal", "Matlalihuitl",
                                    "Mazatl", "Mictlantecuhtli", "Milintica",
                                    "Momoztli", "Namacuix", "Necalli",
                                    "Necuametl", "Nezahualcoyotl", "Nexahualpilli",
                                    "Nochehuatl", "Nopaltzin", "Ollin",
                                    "Quauhtli", "Tenoch", "Teoxihuitl",
                                    "Tepiltzin", "Tezcacoatl", "Tlacaelel",
                                    "Tlacelel", "Tlaloc", "Tlanextic",
                                    "Tlazohtlaloni", "Tlazopillo", "Uetzcayotl",
                                    "Xipilli", "Yaotl"]
            else:
                self.human_names = ["Ahuiliztli", "Atl", "Centehua",
                                    "Chalchiuitl", "Chipahua", "Cihuaton",
                                    "Citlali", "Citlalmina", "Coszcatl",
                                    "Cozamalotl", "Cuicatl", "Eleuia",
                                    "Eloxochitl", "Eztli", "Ichtaca",
                                    "Icnoyotl", "Ihuicatl", "Ilhuitl",
                                    "Itotia", "Iuitl", "Ixcatzin",
                                    "Izel", "Malinalxochitl", "Mecatl",
                                    "Meztli", "Miyaoaxochitl", "Mizquixaual",
                                    "Moyolehuani", "Nahuatl", "Necahual",
                                    "Nenetl", "Nochtli", "Noxochicoztli",
                                    "Ohtli", "Papan", "Patli",
                                    "Quetzalxochitl", "Sacnite", "Teicui",
                                    "Tepin", "Teuicui", "Teyacapan",
                                    "Tlaco", "Tlacoehua", "Tlacotl",
                                    "Tlalli", "Tlanextli", "Xihuitl",
                                    "Xiuhcoatl", "Xiuhtonal",
                                    "Achcauhtli", "Amoxtli", "Chicahua",
                                    "Chimalli", "Cipactli", "Coaxoch",
                                    "Coyotl", "Cualli", "Cuauhtémoc",
                                    "Cuetlachtilo", "Cuetzpalli", "Cuixtli",
                                    "Ehecatl", "Etalpalli", "Huemac",
                                    "Huitzilihuitl", "Iccauhtli", "Ilhicamina",
                                    "Itztli", "Ixtli", "Mahuizoh",
                                    "Manauia", "Matlal", "Matlalihuitl",
                                    "Mazatl", "Mictlantecuhtli", "Milintica",
                                    "Momoztli", "Namacuix", "Necalli",
                                    "Necuametl", "Nezahualcoyotl", "Nexahualpilli",
                                    "Nochehuatl", "Nopaltzin", "Ollin",
                                    "Quauhtli", "Tenoch", "Teoxihuitl",
                                    "Tepiltzin", "Tezcacoatl", "Tlacaelel",
                                    "Tlacelel", "Tlaloc", "Tlanextic",
                                    "Tlazohtlaloni", "Tlazopillo", "Uetzcayotl",
                                    "Xipilli", "Yaotl"]
        else:
            self.human_names = ["other", "something else"]

    def generate_name(self):
        human_name = random.choice(self.human_names)
        return human_name
