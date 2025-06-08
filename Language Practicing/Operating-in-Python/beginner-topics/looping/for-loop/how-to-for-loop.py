# Here you will understand how definite looping works known as for-looping

# ----- Notes/Reminders -----
# range(start, stop, step) → start/stop/step
# integers can ONLY go in those parenthesis for range to work
#
# range(len(sum_list)) v.s. in keyword for sum_list
# For range(len(sum_list)), the 'i' is the number index i.e. 0, 1, 2. Meaning we can only access the numerical represtnation of that item in the list.
# To retrieve the value, i.e. if I want a fruit within the fruit list, i'll use fruits[i = desired fruit]
#
# The 'in' keyword will always access the value through the index. I.e. for i in fruits on new line print(i). The fruits will print.


# Let's try simply using a for loop using range() to return (#'s: 1-5)
print("Looping 5 times with range(5):")
for i in range(5):
    print(i)

# Let's try getting more specifc range() with for looping -> hint: range(start, stop)
# Python language is a last-index-exclusive, meaning the ending index will not be included
print("\nLooping from 1 to 5 using range(1, 6):")
for i in range(1, 6):
    print(i)

# Let's get more specific by looping and counting with range() -> hint: range(start, stop, step)
print("\nCounting down from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

# Now different approach when looping through a list, aka (best practice)
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# Let's try looping through a list using index -> (range(len(list)))
print("\nLooping through a list with index:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

# Let's try ooping through a list with the enumerate() builtin function
print("\nLooping through a list with enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Now let's try looping through a string
word = "hello"
print("\nLooping through each character in a string:")
for char in word:
    print(char)
