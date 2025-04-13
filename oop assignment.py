# oop_assignment.py

# ------------------------------------------
# Assignment 1: Design Your Own Class! 🏗️
# ------------------------------------------

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def specs(self):
        base_specs = super().specs()
        return f"{base_specs}, Cooling System: {self.cooling_system}"

# Testing Assignment 1
print("=== Assignment 1: Smartphone ===")
phone1 = Smartphone("Samsung", "Galaxy A52", 128)
phone1.power_on()
print(phone1.specs())
phone1.power_off()

gaming_phone = GamingPhone("Asus", "ROG Phone 5", 256, "Advanced Vapor Chamber")
gaming_phone.power_on()
print(gaming_phone.specs())
gaming_phone.power_off()

# ------------------------------------------
# Activity 2: Polymorphism Challenge 🎭
# ------------------------------------------

class Vehicle:
    def move(self):
        print("This vehicle moves in its own way.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Testing Activity 2
print("\n=== Activity 2: Vehicle Polymorphism ===")
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
