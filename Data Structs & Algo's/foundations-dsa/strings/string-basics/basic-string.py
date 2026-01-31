''' 
STRING BASICS – CREATION & FUNDAMENTALS

Strings are one of the most common data types in DSA problems.
Let's get comfortable with how strings are created, stored, and accessed.

In Python:
- A string is an immutable sequence of characters
- Characters are indexed (0-based)
- Strings can be iterated like arrays
'''

# 1. CREATING STRINGS

# We can use 'single' and "double" quotes to declare strings
s1 = 'hello' # Using single quotes
s2 = "world" # Using double quotes

print(s1, s2) # single & double quotes don't change print

# Small note: 
# - Use single quotes if your string contains double quotes
# - Use double quotes if your string contains apostrophes
s1 = 'He said "practice daily"'
s2 = "I'm learning DSA"


# There's MULTI-LINE STRINGS
multi_line = """
This is a multi-line string.
It preserves line breaks.
Often used for documentation or long text.
"""
print(multi_line)


# 2. CONVERTING OTHER TYPES -> STRINGS 
num = 42 # int
num_str = str(num) # casting an int -> string
print(num_str, type(num_str)) # Output: 456 <class 'str'>

value = True # bool
bool_str = str(value) # casting an bool -> string
print(bool_str) # Output: True


# 4. DEALING WITH EMPTY STRINGS
empty = ""
print(len(empty)) # Output: 0

# Common in DSA as an initial value
result = ""


# 5. STRINGS LENGTH
word = "algorithm"
print(len(word)) # Output: 9


# 6. STRINGS ARE LIKE SEQUENCES
# - Strings behave like arrays of characters
text = "abc"
print(text[0]) # Output: 'a'
print(text[1]) # Output: 'b'
print(text[2]) # Output: 'c'

# Negative indexing (starts from the end)
print(text[-1])  # Output: 'c'
print(text[-2])  # Output: 'b'
print(text[-3])  # Output: 'a'
print(text[-4])  # This would cause an IndexError: string index out of range


# 7. ITERATING OVER A STRING
# accesses each character in "cat"
for char in "cat":
    print(char) # prints each character on a new line
# Output: c
# Output: a
# Output: t

# With index
word = "data"
for i in range(len(word)):
    print(i, "->", word[i])
# Output: 0 -> d
# Output: 1 -> a
# Output: 2 -> t
# Output: 3 -> a


# 8. IMPORTANT DSA NOTE
"""
In DSA problems:
- Strings are often treated like arrays
- You frequently scan them left to right
- Indexing and iteration must be second nature

Master this before:
- Sliding Window
- Two Pointers
- Frequency Counting
"""
