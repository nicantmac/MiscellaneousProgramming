# Understanding the basics of classes, attributes, methods and instantiating attributes in Python

# --- Defining a simple class ---
# Let's start by creating simple class called Dog
class Dog:
    # __init__ = A special method in Python classes that runs automatically when a new object is created. It sets the initial state of the object.
    # self = A reference to the current instance of the class. It allows access to the object’s attributes and methods.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method (function that belongs to the class)
    def bark(self): # self in parameter makes the method "aware" of which object it's working on, giving access to that object’s attributes
        print(f"{self.name} says: Woof!")

    def get_age(self):
        return f"{self.name} is {self.age} years old."


# ---- Using the class ----

# Here's the anatomy of creating instances (objects)
# Make a variable, and stored inside is the class name with information as its arguements 
dog1 = Dog("Buddy", 5)
dog2 = Dog("Bella", 3)

# Here is how to call methods
dog1.bark()
dog2.bark()

# Using the method that only returns won't print, so print() will display the dog's info
print(dog1.get_age())
print(dog2.get_age())


# ---- Creating a class with default values ----
class Cat:
    def __init__(self, name, color="Gray"):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meow!")

# Here we create cat objects
cat1 = Cat("Whiskers")  # Only need name cause it doesn't have a value but color does have one
cat2 = Cat("Mittens", "White")  # Here we change the value already saved from gray to white

cat1.meow()
cat2.meow()


# ---- Inheritance Example ----

# Parent class
class Animal:
    def __init__(self, species):  # again, __init__ the attributes for Animal
        self.species = species

    def speak(self):
        print(f"I am a {self.species}.")

# Below is the anatomy of child class inherit from Animal
class Bird(Animal):  # the parent class has to be in the parameter if you want to inherit from it
    def __init__(self, name):
        super().__init__("Bird")  # the super() will go to the parent class, and __init__("Bird") will run the parent’s constructor with "Bird" as input
        self.name = name

    def sing(self):
        print(f"{self.name} is singing")

# Here we create Bird object
bird = Bird("Tweety")
bird.speak()  # inherited method
bird.sing()   # Bird method

# --- Summary ---
# - Class = template for creating objects
# - __init__() initializes the object
# - self is required to refer to instance variables/methods
# - Inheritance allows child classes to extend parent classes
