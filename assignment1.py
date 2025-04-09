#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

# Base class
class Computer:
    def __init__(self, color, brand):
        self._color = color  # Encapsulated attribute
        self._brand = brand  # Encapsulated attribute

    def power_on(self):
        print("Computer is powering on...")

    def get_details(self):
        return f"Color: {self._color}, Brand: {self._brand}"

# Subclass 1
class Laptop(Computer):
    def __init__(self, color, brand, screen_size):
        # Directly initializing attributes, without calling super()
        self._color = color
        self._brand = brand
        self._screen_size = screen_size

    def power_on(self):  # Method overriding (polymorphism)
        print("Laptop is powering on...")
        print(f"Screen size: {self._screen_size} inches")

    def get_details(self):  # Overriding to include screen size
        return f"Laptop - Color: {self._color}, Brand: {self._brand}, Screen size: {self._screen_size} inches"

# Subclass 2
class Desktop(Computer):
    def __init__(self, color, brand, tower_size):
        # Directly initializing attributes, without calling super()
        self._color = color
        self._brand = brand
        self._tower_size = tower_size

    def power_on(self):  # Method overriding (polymorphism)
        print("Desktop is powering on...")
        print(f"Tower size: {self._tower_size} liters")

    def get_details(self):  # Overriding to include tower size
        return f"Desktop - Color: {self._color}, Brand: {self._brand}, Tower size: {self._tower_size} liters"

# Demonstrating polymorphism
devices = [
    Laptop("white", "HP", 15.6),
    Desktop("black", "Dell", 25)
]

for device in devices:
    print(device.get_details())  # Polymorphic behavior
    device.power_on()