# Here is a simple dictionary where we will manipulate it in different ways
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

# To print an specific value, simply type the key in the dictionary
print(my_dict["name"])  # Output: Alice

# .get() is a safer way to access dictionary values compared to using bracket notation, it returns a default value if the key is not found
name = my_dict.get("name")
print(name)  # Output: Alice

# To add a new key-value, give it a name in square brackets and type a value
my_dict["job"] = "Engineer"  # adds new key-value pair

# To update a value inside a dictionary, target the key and just change the value
my_dict["age"] = 26 

# When deleting an key-value in a dictionary, the 'del' keyword becomes very useful
del my_dict["city"]

# To check if an key exists within a dictionary
if "name" in my_dict:
    print("Name is present!")

# To see all key: values in an dictionary, just loop through the dictionary
for key, value in my_dict.items():
    print(key, ": ", value)


# Safe example of looping (copy keys first):
print("\nSafe way to modify dict during iteration:")
for key in list(my_dict.keys()):
    if key == "city":
        my_dict["country"] = "USA"

print(my_dict)
