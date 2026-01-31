"""
STRING SLICING

Slicing lets you extract substrings from a string
WITHOUT writing loops.

Syntax:
    string[start : end : step]

- start → inclusive
- end   → exclusive
- step  → how much to jump
"""


# 1. BASIC SLICING
s = "algorithm"
print(s[0:4])   # Output: "algo"
print(s[1:5])   # Output: "lgor"
print(s[:4])    # Output: "algo"  (start defaults to 0)
print(s[4:])    # Output: "rithm" (end defaults to len)


# 2. SLICING WITH NEGATIVE INDICES 
s = "algorithm"
print(s[-5:])  # Output: "rithm"
print(s[:-5])  # Output: "algo"
"""
Negative indices count from the end.
Very useful for suffix problems.
"""


# 3. SLICING WITH STEP
text = "abcdefg"
print(text[::1])   # "abcdefg"
print(text[::2])   # "aceg"
print(text[1::2])  # "bdf"
"""
Step allows skipping characters.
Common in pattern problems.
"""


# 4. REVERSING A STRING (CLASSIC INTERVIEW TRICK)
word = "racecar"
reversed_word = word[::-1] # step through the string from -1 -> 0, so (backwards)
print(reversed_word) # Output: will be "racecar" because it's a palindrome
"""
[::-1] means:
- start from end
- go to the beginning
- move backwards by 1
"""


# 5. PALINDROME CHECK USING SLICING
def is_palindrome(s):
    return s == s[::-1] 
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
"""
Fast and clean, but:
- Uses extra memory
- Not always ideal for very large strings
"""


# 6. SUBSTRING EXTRACTION
email = "user@example.com"

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(username)
print(domain)


# 7. SLICING DOES NOT MODIFY ORIGINAL STRING
original = "data"
slice_part = original[:2]

print(original)   # Output: "data"
print(slice_part) # Output: "da"
"""
Because strings are immutable,
slicing ALWAYS creates a new string.
"""


# 8. COMMON DSA USE CASES
"""
Slicing is useful for:
- Substring problems
- Prefix / suffix checks
- Reversals
- Quick comparisons

Avoid slicing when:
- You need O(1) space
- The string is extremely large
"""


# 9. PREFIX & SUFFIX CHECKS
word = "unhappy"
print(word[:2] == "un")   # Output: True
print(word[-3:] == "ppy") # Output: True


# 10. INTERVIEW TIP
"""
If you use slicing in an interview:
- Explain time & space complexity
- Mention immutability
- Be ready to implement without slicing if asked
"""
