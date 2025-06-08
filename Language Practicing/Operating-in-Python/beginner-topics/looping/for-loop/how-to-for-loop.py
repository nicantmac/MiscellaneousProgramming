# Here you will understand how definite looping works known as for-looping

# 1️⃣ Basic for loop using range()
print("Looping 5 times with range(5):")
for i in range(5):
    print(i)

# 2️⃣ For loop with custom range(start, stop)

print("\nLooping from 1 to 5 using range(1, 6):")
for i in range(1, 6):
    print(i)

# 3️⃣ Counting down with range(start, stop, step)

print("\nCounting down from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

# 4️⃣ Looping through a list (best practice)

fruits = ["apple", "banana", "cherry"]

print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# 5️⃣ Looping through a list using index (range(len(list)))

print("\nLooping through a list with index:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# 6️⃣ Looping through a list with enumerate() (Pythonic!)

print("\nLooping through a list with enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 7️⃣ Looping through a string

word = "hello"

print("\nLooping through each character in a string:")
for char in word:
    print(char)
