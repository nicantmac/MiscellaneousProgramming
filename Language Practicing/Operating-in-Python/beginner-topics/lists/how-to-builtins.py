# Practice with the common built-in functions in Python

# The len() function returns length of objects
my_list = [1, 2, 3, 4]
print(f"Length of list: {len(my_list)}")  # Output: Length of list: 4

# The type() function returns type of objects
x = 42
print(f"Type of x: {type(x)}")  # Output: Type of x: <class 'int'>

# The int(), float(), str() function does type conversions
my_str = "123"
my_int = int(my_str)
print(f"String to integer: {my_int}")  # Output: String to integer: 123

# The sorted() function returns a new sorted list
numbers = [4, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")  # Output: Sorted list: [1, 2, 4, 9]

# The sum() function sums of iterable objects
total = sum([1, 2, 3, 4, 5])
print(f"Sum of list: {total}")  # Output: Sum of list: 15

# The max() & min() function take the max/min of an element
print(f"Max: {max(numbers)}")  # Output: Max: 9
print(f"Min: {min(numbers)}")  # Output: Min: 1

# The range() function generates a range of numbers
for i in range(5):
    print(f"Range number: {i}")  # Output: Range number: (each number in loop)

# The abs() function retrieves the absolute value
print(f"Absolute value of -7: {abs(-7)}")  # Output: Absolute value of -7: 7
