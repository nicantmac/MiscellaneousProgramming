## Here is practice on demonstrating built-in functions and dictionary methods in Python
# The dictionary below is what's going to be manipulated
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# --- BUILT-IN FUNCTIONS ---

# len() -> number of keys
print("len():", len(my_dict))  # 3

# type() -> check type
print("type():", type(my_dict))  # <class 'dict'>

# str() -> string representation
print("str():", str(my_dict))  # String of the dict

# sorted() -> sort keys (returns a list of sorted keys)
print("sorted():", sorted(my_dict))  # ['age', 'city', 'name']

# list() -> convert keys to list
print("list():", list(my_dict))  # ['name', 'age', 'city']
