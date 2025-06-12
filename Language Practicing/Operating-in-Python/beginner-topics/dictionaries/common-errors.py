# Here is practice on basic ways to deal with dictionaries
# The dictionary below is what's going to be manipulated
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# ----- Notes/Reminders -----
# Using try and except error blocks will help so that errors don't crash the program.
#
# ------------

# In Python, a KeyError is an exception that occurs when trying to access an item in a dictionary where it does not exist
print("\nKeyError example: ")
try:
    print(my_dict["country"])  # KeyError -> "country" is not a key in the dictionary
except KeyError:
    # Inside the except block, we can catch the KeyError and print a message
    print("KeyError caught! 'country' key does not exist.")

# A ValueError occurs when a function receives the right type of argument, but the value itself is not appropriate or cannot be processed as expected
print("\nValueError example:")
try:
    value = my_dict["name"]  # value will be "Alice"
    number = int(value)  # ValueError -> "Alice" cannot be converted to an integer
except ValueError:
    # Inside the except block, catch the ValueError and print a message
    print("ValueError caught! Cannot convert 'name' value to integer.")

# A TypeError occurs when an operation or function is applied to an object of an inappropriate type, an example, adding a string and an integer
print("\nTypeError example (invalid key):")
try:
    my_dict[[1, 2, 3]] = "Invalid key"  # TypeError -> lists are unhashable and cannot be used as dictionary keys
except TypeError:
    # Inside the except block, catch the TypeError and print a message
    print("TypeError caught! Cannot use a list as a dictionary key.")

# An AttributeError occurs when you try to access or call an attribute or method that an object does not have, an example, trying to use .append() on a dictionary
print("\nAttributeError example:")
try:
    my_dict.append("oops")  # AttributeError -> dictionaries do not have an append() method (only lists do)
except AttributeError:
    # Inside the except block, catch the AttributeError and print a message
    print("AttributeError caught! Dictionary has no 'append' method.")

print("\nRuntimeError example (modifying during iteration):")
try:
    for key in my_dict:
        if key == "city":
            my_dict["country"] = "USA"  # RuntimeError -> modifying dictionary size during iteration is not allowed
except RuntimeError:
    # Inside the except block, catch the RuntimeError and print a message
    print("RuntimeError caught! Changed dict size during iteration.")
