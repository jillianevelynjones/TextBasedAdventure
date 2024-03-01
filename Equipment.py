class Ammunition():
    name = "Ammunition"


class Arrow(Ammunition):
    name = "Arrow"
    cost = 5, 0, 0
    weight = 1/20

class BlowgunNeedles(Ammunition):
    name = "Blowgun Needles"
    cost = 2, 0, 0
    weight = 1/50

class CrowbowBolts(Ammunition):
    name = "Crossbow Bolts"
    cost = 5, 0, 0
    weight = 1.5/20

class SlingBullets(Ammunition):
    name = "Sling Bullets"
    cost = .2, 0, 0
    weight = 1.5/20

class SpellcastingFocus():
    name = "Spellcasting Focus"

class Crystal(SpellcastingFocus):
    name = "Crystal"
    cost = 0, 0, 10
    weight = 1

class Orb(SpellcastingFocus):
    name = "Orb"
    cost = 0, 0, 20
    weight = 3

class Rod(SpellcastingFocus):
    name = "Rod"
    cost = 0, 0, 10
    weight = 2

class Staff(SpellcastingFocus):
    name = "Staff"
    cost = 0, 0, 5
    weight = 4

class Wand(SpellcastingFocus):
    name = "Wand"
    cost = 0, 0, 10
    weight = 1

class SprigOfMistletoe(SpellcastingFocus):
    name = "Sprig of Mistletoe"
    cost = 0, 0, 1
    weight = 0

class Totem(SpellcastingFocus):
    name = "Totem"
    cost = 0, 0, 1
    weight = 0

class WoodenStaff(SpellcastingFocus):
    name = "Wooden Staff"
    cost = 0, 0, 5
    weight = 4

class YewWand(SpellcastingFocus):
    name = "Yew Wand"
    cost = 0, 0, 10
    weight = 1

class Amulet(SpellcastingFocus):
    name = "Amulet"
    cost = 0, 0, 5
    weight = 1

class Emblem(SpellcastingFocus):
    name = "Emblem"
    cost = 0, 0, 5
    weight = 0

class Reliquary(SpellcastingFocus):
    name = "Reliquary"
    cost = 0, 0, 5
    weight = 2

class Abacus():
    name = "Abacus"
    cost = 0, 0, 2
    weight = 2

class Acid():
    name = "Vial of Acid"
    cost = 0, 0, 25
    weight = 1
    description = "As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact. In either case, make a ranged attack against a creature or object, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage."

class AlchemistFire():
    name = "Flask of Alchemist's Fire"
    cost = 0, 0, 50
    weight = 1
    description = "This sticky, adhesive fluid ignites when exposed to air. As an action, you can throw this flask up to 20 feet, shattering it on impact. Make a ranged attack against a creature or object, treating the alchemist’s fire as an improvised weapon. On a hit, the target takes 1d4 fire damage at the start of each of its turns. A creature can end this damage by using its action to make a DC 10 Dexterity check to extinguish the flames."

class AntiToxin():
    name = "Vial of Antitoxin"
    cost = 0, 0, 50
    weight = 0
    description = "A creature that drinks this vial of liquid gains advantage on saving throws against poison for 1 hour. It confers no benefit to undead or constructs."

class Backpack():
    name = "Backpack"
    cost = 0, 0, 2
    weight = 5

class Ballbearings():
    name = "Bag of 1,000 Ball Bearings"
    cost = 0, 0, 1
    weight = 2
    description = "As an action, you can spill these tiny metal balls from their pouch to cover a level, square area that is 10 feet on a side. A creature moving across the covered area must succeed on a DC 10 Dexterity saving throw or fall prone. A creature moving through the area at half speed doesn’t need to make the save."

class Barrel():
    name = "Barrel"
    cost = 0, 0, 2
    weight = 70

class Basket():
    name = "Basket"
    cost = 0, 4, 0
    weight = 2

class Bedroll():
    name = "Bedroll"
    cost = 0, 0, 1
    weight = 7

class Bell():
    name = "Bell"
    cost = 0, 0, 1
    weight = 0

class Blanket():
    name = "Blanket"
    cost = 0, 5, 0
    weight = 3

class BlockTackle():
    name = "Block and Tackle"
    cost = 0, 0, 1
    weight = 5
    description = " A set of pulleys with a cable threaded through them and a hook to attach to objects, a block and tackle allows you to hoist up to four times the weight you can normally lift."

class Book():
    name = "Book"
    cost = 0, 0, 25
    weight = 5

class Bottle():
    name = "Glass Bottle"
    cost = 0, 0, 2
    weight = 2

class Bucket():
    name = "Bucket"
    cost = 5, 0, 0
    weight = 2

class Caltrops():
    name = "Bag of 20 Caltrops"
    cost = 0, 0, 1
    weight = 2
    description = "As an action, you can spread a bag of caltrops to cover a square area that is 5 feet on a side. Any creature that enters the area must succeed on a DC 15 Dexterity saving throw or stop moving this turn and take 1 piercing damage. Taking this damage reduces the creature’s walking speed by 10 feet until the creature regains at least 1 hit point. A creature moving through the area at half speed doesn’t need to make the save."

class Candle():
    name = "Candle"
    cost = 1, 0, 0
    weight = 0
    description = "For 1 hour, a candle sheds bright light in a 5-foot radius and dim light for an additional 5 feet."

class CrossbowBoltCase():
    name = "Crossbow Bolt Case"
    cost = 0, 0, 1
    weight = 1
    description = "This wooden case can hold up to twenty crossbow bolts."

class ScrollCase():
    name = "Scroll Case"
    cost = 0, 0, 1
    weight = 1
    description = "This cylindrical leather case can hold up to ten rolled-up sheets of paper or five rolled-up sheets of parchment."

class Chain():
    name = "10 feet of Chain"
    cost = 0, 0, 5
    weight = 10
    description = "A chain has 10 hit points. It can be burst with a successful DC 20 Strength check."

class Chalk():
    name = "1 Piece of Chalk"
    cost = 1, 0, 0
    weight = 0

class Chest():
    name = "Chest"
    cost = 0, 0, 5
    weight = 25

class ClimbersKit():
    name = "Climber's Kit"
    cost = 0, 0, 25
    weight = 12
    description = "A climber’s kit includes special pitons, boot tips, gloves, and a harness. You can use the climber’s kit as an action to anchor yourself; when you do, you can’t fall more than 25 feet from the point where you anchored yourself, and you can’t climb more than 25 feet away from that point without undoing the anchor."

class CommonClothes():
    name = "Common Clothes"
    cost = 0, 5, 0
    weight = 3

class Costume():
    name = "Costume"
    cost = 0, 0, 5
    weight = 4

class FineClothes():
    name = "Fine Clothes"
    cost = 0, 0, 15
    weight = 6

class TravelersClothes():
    name = "Traveler's Clothes"
    cost = 0, 0, 2
    weight = 4

class ComponentPouch():
    name = "Component Pouch"
    cost = 0, 0, 25
    weight = 2

class Crowbar():
    name = "Crowbar"
    cost = 0, 0, 2
    weight = 5
    description = "Using a crowbar grants advantage to Strength checks where the crowbar’s leverage can be applied."

class FishingTackle():
    name = "Fishing Tackle"
    cost = 0, 0, 1
    weight = 4
    description = "This kit includes a wooden rod, silken line, corkwood bobbers, steel hooks, lead sinkers, velvet lures, and narrow netting."

class Flask():
    name = "Flask"
    cost = 2, 0, 0
    weight = 1

class Tankard():
    name = "Tankard"
    cost = 2, 0, 0
    weight = 1

class GrapplingHook():
    name = "Grappling Hook"
    cost = 0, 0, 2
    weight = 4

class Hammer():
    name = "Hammer"
    cost = 0, 0, 1
    weight = 3

class SledgeHammer():
    name = "Sledge Hammer"
    cost = 0, 0, 2
    weight = 10

class HealersKit():
    name = "Healer's Kit"
    cost = 0, 0, 5
    weight = 3
    description = "This kit is a leather pouch containing bandages, salves, and splints. The kit has ten uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check."

class HolyWater():
    name = "Holy Water"
    cost = 0, 0, 25
    weight = 1
    description = "As an action, you can splash the contents of this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. In either case, make a ranged attack against a target creature, treating the holy water as an improvised weapon. If the target is a fiend or undead, it takes 2d6 radiant damage."

class Hourglass():
    name = "Hourglass"
    cost = 0, 0, 25
    weight = 1

class HuntingTrap():
    name = "Hunting Trap"
    cost = 0, 0, 5
    weight = 25
    description = "When you use your action to set it, this trap forms a saw-toothed steel ring that snaps shut when a creature steps on a pressure plate in the center. The trap is affixed by a heavy chain to an immobile object, such as a tree or a spike driven into the ground. A creature that steps on the plate must succeed on a DC 13 Dexterity saving throw or take 1d4 piercing damage and stop moving. Thereafter, until the creature breaks free of the trap, its movement is limited by the length of the chain (typically 3 feet long). A creature can use its action to make a DC 13 Strength check, freeing itself or another creature within its reach on a success. Each failed check deals 1 piercing damage to the trapped creature."

class Ink():
    name = "Bottle of Ink"
    cost = 0, 0, 10
    weight = 0

class Pen():
    name = "Ink Pen"
    cost = 2, 0, 0
    weight = 0

class Jug():
    name = "Jug"
    cost = 2, 0, 0
    weight = 4

class Ladder():
    name = "10ft Ladder"
    cost = 0, 1, 0
    weight = 25

class Lamp():
    name = "Lamp"
    cost = 0, 5, 0
    weight = 1
    description = "A lamp casts bright light in a 15-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil."

class BullseyeLantern():
    name = "Bullseye Lantern"
    cost = 0, 0, 10
    weight = 2
    description = "A bullseye lantern casts bright light in a 60-foot cone and dim light for an additional 60 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil."

class HoodedLantern():
    name = "Hooded Lantern"
    cost = 0, 0, 5
    weight = 2
    description = "A hooded lantern casts bright light in a 30-foot radius and dim light for an additional 30 feet. Once lit, it burns for 6 hours on a flask (1 pint) of oil. As an action, you can lower the hood, reducing the light to dim light in a 5-foot radius."

class Lock():
    name = "Lock"
    cost = 0, 0, 10
    weight = 1
    description = "A key is provided with the lock. Without the key, a creature proficient with thieves’ tools can pick this lock with a successful DC 15 Dexterity check."

class MagnifyingGlass():
    name = "Magnifying Glass"
    cost = 0, 0, 100
    weight = 0
    description = "This lens allows a closer look at small objects. It is also useful as a substitute for flint and steel when starting fires. Lighting a fire with a magnifying glass requires light as bright as sunlight to focus, tinder to ignite, and about 5 minutes for the fire to ignite. A magnifying glass grants advantage on any ability check made to appraise or inspect an item that is small or highly detailed."

class Manacles():
    name = "Manacles"
    cost = 0, 0, 2
    weight = 6
    description = "These metal restraints can bind a Small or Medium creature. Escaping the manacles requires a successful DC 20 Dexterity check. Breaking them requires a successful DC 20 Strength check. Each set of manacles comes with one key. Without the key, a creature proficient with thieves’ tools can pick the manacles’ lock with a successful DC 15 Dexterity check. Manacles have 15 hit points."

class MessKit():
    name = "Mess Kit"
    cost = 0, 2, 0
    weight = 1
    description = " This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl."

class Mirror():
    name = "Mirror"
    cost = 0, 0, 5
    weight = .5

class Oil():
    name = "Flask of Oil"
    cost = 0, 1, 0
    weight = 1
    description = "Oil usually comes in a clay flask that holds 1 pint. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn."

class Paper():
    name = "Sheet of Paper"
    cost = 0, 2, 0
    weight = 0

class Parchment():
    name = "Sheet of Parchment"
    cost = 0, 1, 0
    weight = 0

class Perfume():
    name = "Vial of Perfume"
    cost = 0, 0, 5
    weight = 0

class MinersPick():
    name = "Miner's Pick"
    cost = 0, 0, 2
    weight = 10

class Piton():
    name = "Piton"
    cost = 5, 0, 0
    weight = .25

class BasicPoison():
    name = "Vial of Basic Poison"
    cost = 0, 0, 100
    weight = 0
    description = "You can use the poison in this vial to coat one slashing or piercing weapon or up to three pieces of ammunition. Applying the poison takes an action. A creature hit by the poisoned weapon or ammunition must succeed on a DC 10 Constitution saving throw or take 1d4 poison damage. Once applied, the poison retains potency for 1 minute before drying."

class Pole():
    name = "10 ft Pole"
    cost = 5, 0, 0
    weight = 7

class IronPot():
    name = "Iron Pot"
    cost = 0, 0, 2
    weight = 10

class Pouch():
    name = "Pouch"
    cost = 0, 5, 0
    weight = 1
    description = "A cloth or leather pouch can hold up to 20 sling bullets or 50 blowgun needles, among other things."

class Quiver():
    name = "Quiver"
    cost = 0, 0, 1
    weight = 1
    description = "A quiver can hold up to 20 arrows."

class PortableRam():
    name = "Portable Ram"
    cost = 0, 0, 4
    weight = 35
    description = "You can use a portable ram to break down doors. When doing so, you gain a +4 bonus on the Strength check. One other character can help you use the ram, giving you advantage on this check."

class Rations():
    name = "1 Days Rations"
    cost = 0, 5, 0
    weight = 2

class Robes():
    name = "Robes"
    cost = 0, 0, 1
    weight = 4

class HempenRope():
    name = "50ft Hempen Rope"
    cost = 0, 0, 1
    weight = 10

class SilkRope():
    name = "50 ft Silk Rope"
    cost = 0, 0, 10
    weight = 5

class Sack():
    name = "Sack"
    cost = 1, 0, 0
    weight = .5

class Scale():
    name = "Merchant's Scale"
    cost = 0, 0, 5
    weight = 3

class SealingWax():
    name = "Sealing Wax"
    cost = 0, 5, 0
    weight = 0

class Shovel():
    name = "Shovel"
    cost = 0, 0, 2
    weight = 5

class SignalWhistle():
    name = "Signal Whistle"
    cost = 5, 0, 0
    weight = 0

class SignetRing():
    name = "Signet Ring"
    cost = 0, 0, 5
    weight = 0

class Soap():
    name = "Soap"
    cost = 2, 0, 0
    weight = 0

class Spellbook():
    name = "Spellbook"
    cost = 0, 0, 50
    weight = 3

class IronSpikes():
    name = "10 Iron Spikes"
    cost = 0, 0, 1
    weight = 5

class Spyglass():
    name = "Spyglass"
    cost = 0, 0, 1000
    weight = 1

class Tent():
    name = "Two Person Tent"
    cost = 0, 0, 2
    weight = 20

class Tinderbox():
    name = "Tinderbox"
    cost = 0, 5, 0
    weight = 1

class Torch():
    name = "Torch"
    cost = 1, 0, 0
    weight = 1
    description = "A torch burns for 1 hour, providing bright light in a 20-foot radius and dim light for an additional 20 feet. If you make a melee attack with a burning torch and hit, it deals 1 fire damage."

class Vial():
    name = "Vial"
    cost = 0, 0, 1
    weight = 0

class Waterskin():
    name = "Waterskin"
    cost = 0, 2, 0
    weight = 5

class Whetstone():
    name = "Whetstone"
    cost = 1, 0, 0
    weight = 1
