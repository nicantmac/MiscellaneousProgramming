# classes_tutorial.py
# Basic tutorial on defining and using classes in Python

# --- Defining a simple class ---

class Dog:
    # Constructor method (called when you create an object)
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    # Method (function that belongs to the class)
    def bark(self):
        print(f"{self.name} says: Woof!")

    def get_info(self):
        return f"{self.name} is {self.age} years old."

# --- Using the class ---

# Create instances (objects) of Dog
dog1 = Dog("Buddy", 5)
dog2 = Dog("Bella", 3)

# Call methods
dog1.bark()
dog2.bark()

# Get info
print(dog1.get_info())
print(dog2.get_info())

# --- Class with default values ---

class Cat:
    def __init__(self, name, color="Gray"):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meow!")

# Create cats
cat1 = Cat("Whiskers")
cat2 = Cat("Mittens", "White")

cat1.meow()
cat2.meow()

# --- Inheritance Example ---

# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"I am a {self.species}.")

# Child class (inherits from Animal)
class Bird(Animal):
    def __init__(self, name):
        super().__init__("Bird")  # call parent class constructor
        self.name = name

    def sing(self):
        print(f"{self.name} is singing 🎶")

# Create Bird object
bird = Bird("Tweety")
bird.speak()  # inherited method
bird.sing()   # Bird method

# --- Summary ---
# - Class = template for creating objects
# - __init__() initializes the object
# - self is required to refer to instance variables/methods
# - Inheritance allows child classes to extend parent classes
