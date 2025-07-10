import json
import os

class MenuManager:
    def __init__(self, file_path="menu.json"):
        self.file_path = file_path
        self.menu = self.load_menu()
        
    def load_menu(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return {}
        
    def save_menu(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.menu, file, indent=4)
    
    def add_item(self, item_id: str, item):
        self.menu[item_id] = item
        self.save_menu()
        
    def remove_item(self, item_id: str):
        if item_id in self.menu:
            del self.menu[item_id]
            self.save_menu()
        else:
            print(f"Item {item_id} not found in menu.")
            
    def update_item(self, item_id: str, item):
        if item_id in self.menu:
            self.menu[item_id] = item
            self.save_menu()
        else:
            print(f"Item {item_id} not found in menu.")
            
    def show_menu(self):
        if not self.menu:
            print("El menú está vacío.")
            return
        print("Menú:")
        for item_id, item in self.menu.items():
            print(f"{item_id}: {item['name']} - ${item['price']:.2f}")
