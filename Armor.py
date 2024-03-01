class Shield:
    """A shield that can be worn on one hand."""

    name = "Shield"
    cost = 0, 0, 10 # cp, sp, gp
    base_armor_class = 2
    weight = 6  # In lbs

    def __str__(self):
        return self.name


class NoShield(Shield):
    """If a character is carrying no shield."""

    name = "No shield"
    cost = 0, 0, 0
    base_armor_class = 0

    def __str__(self):
        return self.name


class Armor:
    name = "Unknown Armor"
    cost = 0, 0, 0
    base_armor_class = 10
    dexterity_mod_max = None
    dexterity_applied = True
    strength_required = None
    stealth_disadvantage = False
    weight = 0  # In lbs

    def __str__(self):
        return self.name


class NoArmor(Armor):
    name = "No Armor"


class LightArmor(Armor):
    name = "Light Armor"


class MediumArmor(Armor):
    name = "Medium Armor"


class HeavyArmor(Armor):
    name = "Heavy Armor"
    dexterity_applied = False


class PaddedArmor(LightArmor):
    name = "Padded Armor"
    cost = 0, 0, 5
    base_armor_class = 11
    weight = 8
    stealth_disadvantage = True


class LeatherArmor(LightArmor):
    name = "Leather Armor"
    cost = 0, 0, 10
    base_armor_class = 11
    weight = 10


class StuddedLeatherArmor(LightArmor):
    name = "Studded Leather Armor"
    cost = 0, 0, 45
    base_armor_class = 12
    weight = 13


class HideArmor(MediumArmor):
    name = "Hide Armor"
    cost = 0, 0, 10
    base_armor_class = 12
    dexterity_mod_max = 2
    weight = 12


class ChainShirt(MediumArmor):
    name = "Chain Shirt"
    cost = 0, 0, 50
    base_armor_class = 13
    dexterity_mod_max = 2
    weight = 20


class ScaleMail(MediumArmor):
    name = "Scale Mail"
    cost = 0, 0, 50
    base_armor_class = 14
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 45


class Breastplate(MediumArmor):
    name = "Breastplate"
    cost = 0, 0, 400
    base_armor_class = 14
    dexterity_mod_max = 2
    weight = 20


class HalfPlate(MediumArmor):
    name = "Half Plate"
    cost = 0, 0, 750
    base_armor_class = 15
    dexterity_mod_max = 2
    stealth_disadvantage = True
    weight = 40


class RingMail(HeavyArmor):
    name = "Ring Mail"
    cost = 0, 0, 30
    base_armor_class = 14
    stealth_disadvantage = True
    weight = 40


class ChainMail(HeavyArmor):
    name = "Chain Mail"
    cost = 0, 0, 75
    base_armor_class = 16
    strength_required = 13
    stealth_disadvantage = True
    weight = 55


class SplintArmor(HeavyArmor):
    name = "Splint Armor"
    cost = 0, 0, 200
    base_armor_class = 17
    strength_required = 15
    stealth_disadvantage = True
    weight = 60


class PlateMail(HeavyArmor):
    name = "Plate Mail"
    cost = 0, 0, 1500
    base_armor_class = 18
    strength_required = 15
    stealth_disadvantage = True
    weight = 65



light_armors = [PaddedArmor, LeatherArmor, StuddedLeatherArmor]
medium_armors = [HideArmor, ChainShirt, ScaleMail, Breastplate, HalfPlate]
heavy_armors = [RingMail, ChainMail, SplintArmor, PlateMail]
all_armors = light_armors + medium_armors + heavy_armors
