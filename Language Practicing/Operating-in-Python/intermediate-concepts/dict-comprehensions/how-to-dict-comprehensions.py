# dict_comprehension_tutorial.py
# How to use dictionary comprehension in Python

# {key_expr: value_expr for item in iterable if condition (optional)}

# --- Example 1: Squares of numbers ---

squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- Example 2: Mapping words to their lengths ---

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)
# Result: {'apple': 5, 'banana': 6, 'cherry': 6}

# --- Example 3: Filtered dictionary ---

# Only include even numbers
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even squares:", even_squares)
# Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# --- Example 4: Inverting a dictionary (swap keys and values) ---

original = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for key, value in original.items()}
print("Inverted dictionary:", inverted)
# Result: {1: 'a', 2: 'b', 3: 'c'}

# --- Example 5: Conditional value (if-else inside value) ---

numbers = [1, 2, 3, 4, 5]
parity = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print("Number parity dictionary:", parity)
# Result: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# --- Summary ---
# Dictionary comprehension:
# {key: value for item in iterable if condition (optional)}
# Useful for:
# - Building dictionaries quickly
# - Filtering
# - Transforming values
# - Inverting dictionaries
