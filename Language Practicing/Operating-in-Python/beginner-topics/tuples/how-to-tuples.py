# tuples_howto.py
# How to create and use tuples in Python

# --- Creating tuples ---

# Regular tuple
my_tuple = (1, 2, 3)
print("Regular tuple:", my_tuple)

# Tuple with mixed data types
mixed_tuple = ("hello", 42, 3.14)
print("Mixed tuple:", mixed_tuple)

# Single-element tuple (must have comma)
single_tuple = (99,)
print("Single-element tuple:", single_tuple)

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Convert list to tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)
print("Converted list to tuple:", converted_tuple)

# --- Accessing tuple elements ---

# Indexing
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing
print("Slice of first two elements:", my_tuple[:2])

# --- Immutability ---
# Tuples cannot be changed!
try:
    my_tuple[0] = 100
except TypeError:
    print("❌ Cannot modify tuples! They are immutable.")

# --- Looping through a tuple ---
print("Looping through my_tuple:")
for item in my_tuple:
    print(item)
