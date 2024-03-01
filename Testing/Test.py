import Armor
import Weapons
import Equipment
from Inventory import Inventory_Class

inventory = Inventory_Class()

print(inventory.display_inventory())

print("\n adding Bedroll and Blanket")
inventory.add_item(Equipment.Bedroll(), 1)
inventory.add_item(Equipment.Blanket(), 1)

print(inventory.display_inventory())
