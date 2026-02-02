"""
STRING IMMUTABILITY (VERY IMPORTANT FOR DSA)

In Python, strings are IMMUTABLE.
This means:
- Once a string is created, it CANNOT be changed in place
- Any "modification" creates a NEW string

This behavior is critical in DSA problems.
Many bugs come from forgetting this.
"""

# WHAT IMMUTABLE MEANS
s = "hey"
# s[0] = "H" # Outputs -> TypeError (NOT allowed)

print(s)  # Output is still -> "hey"



# 1. WHY STRINGS ARE IMMUTABLE
"""
Strings are immutable for:
- Performance
- Safety
- Memory optimization

Because strings can't change, Python can safely reuse them.
"""

a = "data"
b = "data"
print(a is b)  # Often True (same memory location)


# 2. "MODIFYING" A STRING ACTUALLY CREATES A NEW ONE
word = "hello"
new_word = word + "!" # changes are stored in new string

print("string 1:", word, "- string 2", new_word) 
# Output: string 1: hello - string 2: hello!

print(word is new_word)  # False


# 3. COMMON BEGINNER MISTAKE
s = "abc"
# Trying to change one character
# s[1] = "x" # Output: TypeError

# Correct way to rebuild a string
s = s[0] + "x" + s[2]
print(s) # Output: "axc"


# 4. IMMUTABILITY IN LOOPS (VERY COMMON DSA PATTERN)
result = ""
for char in "abc":
    result = result + char.upper()
print(result)  # Output: "ABC"

# result = "" -> initialize empty string
# for char in "abc": -> iterates over each character -> 'a', then 'b', then 'c'
# result = result + char.upper() 
''' takes the uppercase of the current char -> concatenates to current value
# of result, and reassigns back to to result. (never tries changing result)'''

# This works, but is inefficient for very large strings.


# 5. BETTER PATTERN: BUILD WITH A LIST
chars = []
for char in "abc":
    chars.append(char.upper())
    # converts the current character to uppercase, 
    # then appends the uppercase char to the chars list

result = "".join(chars)
# .join() takes all items in the list and concatenates them into a single string
print(result)  # "ABC"


# WHY THIS MATTERS IN DSA
"""
In DSA problems:
- You CANNOT modify a string in place
- You must build new strings
- Or track indices instead of changing characters

This affects:
- Sliding Window
- Two Pointers
- String replacement problems
- Palindrome checks
"""

"""
If every asked: "Can you modify this string?"

Correct response:
"No, strings are immutable, so I would create a new string
or use indices to simulate modification."
"""
