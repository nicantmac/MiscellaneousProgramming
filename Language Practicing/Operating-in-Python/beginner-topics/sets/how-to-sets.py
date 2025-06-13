# SImple practice on Python sets
# A set is an unordered collection of unique elements.

# How to create a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# When creating a set, duplicate values are automatically removed
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set removes duplicates:", duplicate_set)

# You can also create an empty set like this
empty_set = set()  # Note: {} creates an empty dictionary, NOT a set. Remember to use the set() function

# To add elements to a set, use the .add() method
my_set.add(6)
print("After adding 6:", my_set)

# To remove an element from a set, use the .remove() method
my_set.remove(3)  # Note: a KeyError raises if the element does not exist
print("After removing 3:", my_set)

# Similar but different from .remove(), the discard method also discards an element (does NOT raise error if element not present)
my_set.discard(10)  # No error even though 10 is not in the set

# To check a value is inside a set
print("Is 4 in the set?", 4 in my_set)

# To loop through a set
print("Looping through set:")
for item in my_set:
    print(item)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: all unique elements in either set
print("Union:", set_a | set_b)

# Intersection: elements common to both sets
print("Intersection:", set_a & set_b)

# Difference: elements in set_a but not in set_b
print("Difference (A - B):", set_a - set_b)

# Symmetric difference: elements in either set, but not both
print("Symmetric difference:", set_a ^ set_b)

# Useful built-in methods
print("Length of set_a:", len(set_a))
set_a.clear()  # Removes all elements
print("Set A after clear:", set_a)

# Summary:
# - Sets store unique items
# - Useful for removing duplicates, testing membership, and performing set operations
# - Sets are unordered → no indexing or slicing
# - Set operations: union (|), intersection (&), difference (-), symmetric difference (^)
