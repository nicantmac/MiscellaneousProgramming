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
print("\n2️⃣ ValueError example:")
try:
    value = my_dict["name"]  # value will be "Alice"
    number = int(value)  # ValueError -> "Alice" cannot be converted to an integer
except ValueError:
    # Inside the except block, catch the ValueError and print a message
    print("❌ ValueError caught! Cannot convert 'name' value to integer.")


print("\n3️⃣ TypeError example (invalid key):")
try:
    my_dict[[1, 2, 3]] = "Invalid key"  # ❌ TypeError → lists are unhashable and cannot be used as dictionary keys
except TypeError:
    # Catching the TypeError and printing a message
    print("❌ TypeError caught! Cannot use a list as a dictionary key.")

print("\n4️⃣ AttributeError example:")
try:
    my_dict.append("oops")  # ❌ AttributeError → dictionaries do not have an append() method (only lists do)
except AttributeError:
    # Catching the AttributeError and printing a message
    print("❌ AttributeError caught! Dictionary has no 'append' method.")

print("\n5️⃣ RuntimeError example (modifying during iteration):")
try:
    for key in my_dict:
        if key == "city":
            my_dict["country"] = "USA"  # ❌ RuntimeError → modifying dictionary size during iteration is not allowed
except RuntimeError:
    # Catching the RuntimeError and printing a message
    print("❌ RuntimeError caught! Changed dict size during iteration.")
