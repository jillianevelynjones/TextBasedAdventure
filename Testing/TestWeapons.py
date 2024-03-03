import re
import random


class Weapons:

    class SimpleMeleeWeapons:

        def __init__(self, name, category,
                     num_dice, dice_value, damage_type,
                     properties, weapon_range, weight, rarity):
            self.name = name
            self.category = category
            self.num_dice = num_dice
            self.dice_value = dice_value
            self.damage_type = damage_type
            self.properties = properties
            self.weapon_range = weapon_range
            self.weight = weight
            self.rarity = rarity

    class SimpleRangedWeapons:

        def __init__(self, name, category,
                     num_dice, dice_value, damage_type,
                     properties, weapon_range, weight, rarity):
            self.name = name
            self.category = category
            self.num_dice = num_dice
            self.dice_value = dice_value
            self.damage_type = damage_type
            self.properties = properties
            self.weapon_range = weapon_range
            self.weight = weight
            self.rarity = rarity

    class MartialMeleeWeapons:

        def __init__(self, name, category,
                     num_dice, dice_value, damage_type,
                     properties, weapon_range, weight, rarity):

            self.name = name
            self.category = category
            self.num_dice = num_dice
            self.dice_value = dice_value
            self.damage_type = damage_type
            self.properties = properties
            self.weapon_range = weapon_range
            self.weight = weight
            self.rarity = rarity


#simple melee weapons
club = Weapons.SimpleMeleeWeapons("Club", "Items", 1, 4, "Bludgeoning", "Light", None, 2, "Standard")
dagger = Weapons.SimpleMeleeWeapons("Dagger", "Items", 1, 4, "Piercing", "Finesse, Light, Range, Thrown", [20, 60], 1, "Standard")
greatclub = Weapons.SimpleMeleeWeapons("Greatclub", "Items", 1, 8, "Bludgeoning", "Two-Handed", None, 10, "Standard")
handaxe = Weapons.SimpleMeleeWeapons("Handaxe", "Items", 1, 6, "Slashing", "Light, Range, Thrown", [20, 60], 2, "Standard")
javelin = Weapons.SimpleMeleeWeapons("Javelin", "Items", 1, 6, "Piercing", "Range, Thrown", [30, 120], 2, "Standard")
light_hammer = Weapons.SimpleMeleeWeapons("Light Hammer", "Items", 1, 4, "Bludgeoning", "Light, Thrown", None, 2, "Standard")
mace = Weapons.SimpleMeleeWeapons("Mace", "Items", 1, 6, "Bludgeoning", None, None, 4, "Standard")
quarterstaff = Weapons.SimpleMeleeWeapons("Quarterstaff", "Items", 1, 6, "Bludgeoning", "Versatile", None, 4, "Standard")
sickle = Weapons.SimpleMeleeWeapons("Sickle", "Items", 1, 4, "Slashing", "Light", None, 2, "Standard")
spear = Weapons.SimpleMeleeWeapons("Spear", "Items", 1, 6, "Piercing", "Range, Thrown, Versatile", [20, 60], 3, "Standard")


simple_melee_weapons = [club, dagger, greatclub,
                  handaxe, javelin, light_hammer,
                  mace, quarterstaff, sickle, spear]


def rolldice(sides, num_rolls):

    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    total = sum(rolls)
    print(f"Rolling {num_rolls}d{sides}: {rolls} -> Total: {total}")
    return total


def test_weapon():

    weapon_name = input("Select a weapon: ")
    pattern = re.compile(f"^{re.escape(weapon_name)}$", re.IGNORECASE)
    weapon = next((w for w in simple_melee_weapons if pattern.match(w.name)), None)
    if weapon:
        print(f"Rolling damage for {weapon.name}:")
        damage = rolldice(weapon.dice_value, weapon.num_dice,)
        print(f"Damage rolled: {damage}")
    else:
        print(f"Weapon {weapon_name} not found in inventory.")


# Example usage
test_weapon()