# Here is a simple dictionary where we will manipulate it in different ways

# In Python, a KeyError is an exception that occurs when trying to access an item in a dictionary where it does not exist
print("\nKeyError example: ")
try:
    print(my_dict["country"])  # KeyError → "country" is not a key
except KeyError:
    print("KeyError caught! 'country' key does not exist.")

print("\n2️⃣ ValueError example:")
try:
    value = my_dict["name"]
    number = int(value)  # ValueError → "Alice" is not a number
except ValueError:
    print("❌ ValueError caught! Cannot convert 'name' value to integer.")

print("\n3️⃣ TypeError example (invalid key):")
try:
    my_dict[[1, 2, 3]] = "Invalid key"  # TypeError → list is unhashable
except TypeError:
    print("❌ TypeError caught! Cannot use a list as a dictionary key.")

print("\n4️⃣ AttributeError example:")
try:
    my_dict.append("oops")  # AttributeError → dict has no append()
except AttributeError:
    print("❌ AttributeError caught! Dictionary has no 'append' method.")

print("\n5️⃣ RuntimeError example (modifying during iteration):")
try:
    for key in my_dict:
        if key == "city":
            my_dict["country"] = "USA"  # Modifying dict during loop
except RuntimeError:
    print("❌ RuntimeError caught! Changed dict size during iteration.")
