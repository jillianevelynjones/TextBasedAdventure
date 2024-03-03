class Inventory_Class:
    def __init__(self):
        self.items = {}
        self.equipped_items = {}

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name][0] += quantity
        else:
            self.items[item.name] = [quantity, item]

    def remove_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name][0] -= quantity
            if self.items[item.name][0] <= 0:
                del self.items[item.name]
        else:
            print(f"{item.name} not found in inventory.")

    def equip_item(self, item_name):
        if item_name in self.items:
            if item_name not in self.equipped_items:
                self.equipped_items[item_name] = self.items[item_name]
                print(f"{item_name} equipped.")
            else:
                print(f"{item_name} is already equipped.")
        else:
            print(f"{item_name} not found in inventory.")

    def display_inventory(self):
        print("Current inventory:")
        for item_name, (quantity, item) in self.items.items():
            print(f"{item_name}: {quantity}")
            print(f"Details: {item.__dict__}\n")

    def display_equipped_items(self):
        print("Equipped items:")
        for item_name, (quantity, item) in self.equipped_items.items():
            print(f"{item_name}: {quantity}")
            print(f"Details: {item.__dict__}\n")

# Example usage
inventory = Inventory_Class()
inventory.add_item()
inventory.add_item(Item("Shield", 5))
inventory.add_item(Item("Helmet", 3))
inventory.display_inventory()

inventory.equip_item("Sword")
inventory.equip_item("Sword")  # Try equipping the same item again
inventory.equip_item("Helmet")
inventory.display_equipped_items()
