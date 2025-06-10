# built-in-functions.py
# Demonstrating useful built-in functions on Python data types


# Numbers
num = -42
print("\nabs():", abs(num))  # Absolute value

print("pow():", pow(2, 3))   # Power: 2^3 = 8

# Strings
s = "hello"
print("\nlen():", len(s))    # Length of string

print("sorted():", sorted(s))  # Sorted list of characters

# Lists
lst = [5, 2, 9, 1]
print("\nmin():", min(lst))  # Minimum value
print("max():", max(lst))    # Maximum value
print("sum():", sum(lst))    # Sum of all elements

# Type conversion
print("\nstr(123):", str(123))  # Number to string
print("int('456'):", int('456'))  # String to number

# Type checking
print("\ntype(3.14):", type(3.14))  # <class 'float'>
