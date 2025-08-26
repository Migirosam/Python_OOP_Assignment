# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged to {self.battery}%")

# Inherited Class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system 🎮")
            self.battery -= 10
        else:
            print("Battery too low to play games!")

# Example objects
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 80)
phone2 = GamingPhone("Asus", "ROG Phone 7", "256GB", 100, "Liquid Cooling")

# Test methods
phone1.make_call("123-456-789")
phone2.play_game("PUBG")
phone2.charge(15)
