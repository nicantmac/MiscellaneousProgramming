# dict_comprehensions.py
# Dictionary comprehensions in Python

# Example: create a dict of squares
squares = {x: x ** 2 for x in range(6)}
print("Squares:", squares)

# Filtered comprehension: only even numbers
even_squares = {x: x ** 2 for x in range(6) if x % 2 == 0}
print("Even squares:", even_squares)

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print("Swapped dict:", swapped)
