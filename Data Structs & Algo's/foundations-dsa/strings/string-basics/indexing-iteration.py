"""
STRING INDEXING & ITERATION

Almost every string DSA problem depends on:
- Accessing characters by index
- Iterating through the string
- Knowing where you are (left, right, middle)

If this feels natural, most problems become easier.
"""

# 1. STRING INDEXING (0-BASED)
s = "python"

# Better visual of index positions:
# p  y  t  h  o  n
# 0  1  2  3  4  5
print(s[0])  # Output: 'p'
print(s[3])  # Output: 'h'
print(s[5])  # Output: 'n'

''' simple indexing retrievals are; the name of the variable 
    followed with [] stating the (in-bound index)) '''


# 2. NEGATIVE INDEXING
''' We can also start from the end of a string and work backwards.
    Negative indices start from the end '''
print(s[-1])  # Output: 'n'
print(s[-2])  # Output: 'o'

# Positive index: left → right
# Negative index: right → left


# 3. STRING LENGTH & BOUNDS 
length = len(s) # Reminder: s = 'python'
print(length)  # Output: 6
print(s[6])  # IndexError -> Index out of range

# Last character
print(s[len(s) - 1])


# 4. BASIC STRING ITERATION
for char in "abc":
    print(char)
# This gives you the character, but NOT the index


# 5. ITERATION WITH INDEX (VERY IMPORTANT)
word = "data"
for i in range(len(word)):
    print(i, "->", word[i])
# Most DSA problems require BOTH: index and character


# 6. ENUMERATE (MORE PYTHONIC & CLEAN)
# enumerate() is extremely useful, it avoids manual index tracking.

for index, char in enumerate("data"):
    print(index, "->", char)
# Output: 0 -> d
# Output: 1 -> a
# Output: 2 -> t
# Output: 3 -> a


# 7. LEFT-TO-RIGHT SCANNING (COMMON DSA PATTERN)
s = "abcdef"

i = 0
while i < len(s):
    print(s[i])
    i += 1
"""
This pattern becomes a combo of two-ptr & slide window:
- left pointer in two pointers
- window start in sliding window
"""


# 8. RIGHT-TO-LEFT SCANNING [Reminder: s = 'python']

# Index visual
# p  y  t  h  o  n
# 0  1  2  3  4  5
i = len(s) - 1 # len(s) -> 6, so minus 1 puts us at 5
while i >= 0:
    print(s[i])
    i -= 1
"""
Used in:
- palindrome checks
- reverse scans
"""


# 9. TWO POINTERS PREVIEW
# Index visual -> s = 'python'
# p  y  t  h  o  n
# 0  1  2  3  4  5

left = 0
right = len(s) - 1
while left < right:
    print(s[left], s[right])
    left += 1
    right -= 1
# the while condition basically keep narrowing the search range until only one element remains
# if the desired element isn't found, a standard convention return -1 means item wasn't found
"""
This is the foundation of problems like:
- palindrome problems
- string reversal
- two-pointer techniques
"""


# 10. IMPORTANT DSA MINDSET
"""
When solving string problems, always ask:
- Where is my index?
- Am I moving left, right, or both?
- Do I need the character, the index, or both?

Index control = problem control.
"""
