# The essential and common built-in functions in Python

# This is the set used for manipulation
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# ----- Built-in functions -----

# len() -> number of elements
print("Length of set:", len(my_set))  # Output: Length of set: 5

# sorted() -> returns a sorted list version of the set (sets themselves are unordered)
print("Sorted set: ", sorted(my_set))  # Output: Sorted set: [1, 2, 3, 4, 5]

# sum() -> sum of elements
print("Sum of set elements:", sum(my_set))  # Output: Sum of set elements: 15

# max() -> largest element
print("Max element:", max(my_set))  # Output: Max element: 5

# min() -> smallest element
print("Min element:", min(my_set))  # Output: Min element: 1
