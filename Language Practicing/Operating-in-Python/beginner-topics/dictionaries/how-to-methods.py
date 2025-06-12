# Here is practice on demonstrating dictionary methods in Python
# The dictionary below is what's going to be manipulated
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# --- DICT METHODS ---

# .keys() -> view keys
print("keys():", my_dict.keys())

# .values() -> view values
print("values():", my_dict.values())

# .items() -> view (key, value) pairs
print("items():", my_dict.items())

# .get() -> safe access
print("get():", my_dict.get("name"))  # Alice
print("get() with missing key:", my_dict.get("country", "Not found"))  # Not found

# .update() -> add or update multiple key-value pairs
my_dict.update({"country": "USA", "age": 26})
print("After update():", my_dict)

# .pop() -> remove and return a value by key
city_value = my_dict.pop("city")
print("After pop('city'):", my_dict)
print("Popped value:", city_value)

# .clear() -> remove all items from dict
my_dict.clear()
print("After clear():", my_dict)
