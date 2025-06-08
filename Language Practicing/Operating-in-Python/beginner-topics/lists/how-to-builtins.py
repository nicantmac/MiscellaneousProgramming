# how-to-builtins.py
# ----------------------------------------
# Common Built-in Functions in Python
# ----------------------------------------

# 1️⃣ len() → returns length of object

my_list = [1, 2, 3, 4]
print(f"Length of list: {len(my_list)}")

# 2️⃣ type() → returns type of object

x = 42
print(f"Type of x: {type(x)}")

# 3️⃣ int(), float(), str() → type conversion

my_str = "123"
my_int = int(my_str)
print(f"String to integer: {my_int}")

# 4️⃣ sorted() → returns a new sorted list

numbers = [4, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

# 5️⃣ sum() → sum of iterable

total = sum([1, 2, 3, 4, 5])
print(f"Sum of list: {total}")

# 6️⃣ max(), min() → max/min element

print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# 7️⃣ range() → generate range of numbers

for i in range(5):
    print(f"Range number: {i}")

# 8️⃣ abs() → absolute value

print(f"Absolute value of -7: {abs(-7)}")
