class Inventory_Class:
    def __init__(self):
        self.items = {}

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

    def display_inventory(self):
        print("Current inventory:")
        for item_name, (quantity, item) in self.items.items():
            print(f"{item_name}: {quantity}")
            print(f"Details: {item.__dict__}\n")
