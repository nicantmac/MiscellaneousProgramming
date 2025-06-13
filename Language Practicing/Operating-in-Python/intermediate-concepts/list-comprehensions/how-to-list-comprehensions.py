# How to use Python List Comprehensions

# --- Basic List Comprehension ---

# Square numbers from 0 to 9
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Create a list of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", evens)

# Create a list of odd numbers
odds = [x for x in range(20) if x % 2 != 0]
print("Odd numbers:", odds)

# --- With Strings ---

words = ["hello", "world", "python", "rocks"]

# Create a list of word lengths
word_lengths = [len(word) for word in words]
print("Word lengths:", word_lengths)

# Convert words to uppercase
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

# --- Nested List Comprehension ---

# Create a multiplication table (flattened)
mult_table = [i * j for i in range(1, 4) for j in range(1, 4)]
print("Multiplication table:", mult_table)

# --- Using if-else inside List Comprehension ---

numbers = [1, 2, 3, 4, 5, 6]

# Label numbers as even or odd
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print("Even or Odd labels:", labels)

# --- Set Comprehension ---

# Unique first letters of words
first_letters = {word[0] for word in words}
print("First letters (set comprehension):", first_letters)

# --- Dictionary Comprehension ---

# Map words to their lengths
word_length_dict = {word: len(word) for word in words}
print("Word length dictionary:", word_length_dict)

# --- Summary ---
# List comprehension:
# [expression for item in iterable if condition]
# Optional: nested comprehensions, if-else inside expression
# Set and dict comprehensions also exist!

