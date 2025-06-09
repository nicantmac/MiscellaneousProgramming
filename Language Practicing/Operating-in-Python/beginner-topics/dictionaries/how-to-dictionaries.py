# dict_errors_demo.py
# Demonstrating common dictionary errors in Python

# Here is a simple dictionary where we will manipulate it in different ways
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict)

print(my_dict["name"])  # Output: Alice

my_dict["job"] = "Engineer"  # adds new key-value pair
my_dict["age"] = 26         # updates value for "age"

# When deleting an key: value in a dictionary, the 'del' keyword becomes very useful
del my_dict["city"]

# To check if an key exists within a dictionary
if "name" in my_dict:
    print("Name is present!")

# To see all key: values in an dictionary, just loop through the dictionary
for key, value in my_dict.items():
    print(key, ": ", value)


print("\n--- Common Errors with Dictionaries ---")
print("\n1️⃣ KeyError example:")
try:
    print(my_dict["country"])  # KeyError → "country" is not a key
except KeyError:
    print("❌ KeyError caught! 'country' key does not exist.")

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

# Safe example of looping (copy keys first):
print("\n✅ Safe way to modify dict during iteration:")
for key in list(my_dict.keys()):
    if key == "city":
        my_dict["country"] = "USA"

print(my_dict)
