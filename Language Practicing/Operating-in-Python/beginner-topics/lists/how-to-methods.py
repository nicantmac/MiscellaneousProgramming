# Common Object Methods in Python

# List methods
fruits = ["apple", "banana", "cherry"]

# append()
fruits.append("orange")
print(f"After append: {fruits}")

# insert()
fruits.insert(1, "kiwi")
print(f"After insert at position 1: {fruits}")

# remove()
fruits.remove("banana")
print(f"After removing 'banana': {fruits}")

# pop()
last_fruit = fruits.pop()
print(f"Popped fruit: {last_fruit}")
print(f"After pop: {fruits}")

# sort() (in-place)
numbers = [4, 2, 7, 1]
numbers.sort()
print(f"Sorted numbers: {numbers}")

# String methods

my_string = "  hello world!  "
# 6️⃣ strip()
print(f"After strip: '{my_string.strip()}'")

# 7️⃣ upper()
print(f"Uppercase: {my_string.upper()}")

# 8️⃣ lower()
print(f"Lowercase: {my_string.lower()}")

# 9️⃣ replace()
new_string = my_string.replace("world", "Python")
print(f"Replaced string: {new_string}")

# 10️⃣ split()
words = my_string.split()
print(f"Split words: {words}")
