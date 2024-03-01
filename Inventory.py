class Inventory_Class:
    
    def __init__(self):
        self.inventory = {}
        self.total_weight = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name][0] += quantity  
        else:
            self.inventory[item.name] = [quantity, item]  

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name][0] -= quantity  
            if self.inventory[item.name][0] <= 0:
                del self.inventory[item.name]  
        else:
            print(f"{item.name} not found in inventory.")

    def display_inventory(self):
        total_weight = 0
        print("\n   Current inventory:")
        for item_name, (quantity, item) in self.inventory.items():
            print(f"      {item_name}: {quantity}")
            total_weight += item.weight * quantity 
        print(f"   Total weight: {total_weight} lbs")

    def get_inventory(self):
        return self.inventory
