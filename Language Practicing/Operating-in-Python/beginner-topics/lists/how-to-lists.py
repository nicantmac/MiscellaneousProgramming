# Here we will practice and understand how Lists function.

# CLet's start things off with simply creating a list
fruits = ["apple", "banana", "grapes", "orange"]
print(f"Original list of fruits: {fruits}")

# Now let's try accessing list elements 
# Let's start with indexing starting at 0, rmeinder python starts from 0 instead of 1
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")

 # When you start to see negative indexing that now means (start from the end going in reverse)
print(f"Last fruit: {fruits[-1]}")

# Below displays if you ever want to modify a list element
fruits[1] = "blueberry"
print(f"Modified list of fruits: {fruits}")

# Now by adding elements to a list in python, .append() method is extremely common
fruits.append("grape")
print(f"After appending 'grape': {fruits}")

# Now specifically inserting elements at a specific position, we can utilize the .insert() method
fruits.insert(2, "kiwi")
print(f"After inserting 'kiwi' at position 2: {fruits}")

# For removing elements, we can utilize the .remove() method
fruits.remove("apple")
print(f"After removing 'apple': {fruits}")

# Whenever popping an element (removes the last element and returns it)
popped_fruit = fruits.pop()
print(f"Popped fruit: {popped_fruit}")
print(f"List after popping: {fruits}")

# To obtain the length of list, simply you can use len() built-in function
print(f"Number of fruits in the list: {len(fruits)}")

# To traverse through lists, we can iterate through a list for looping
print("Iterating through the list:")
for fruit in fruits:
    print(f"- {fruit}")

# There are many ways to sorting lists, however quickly we can use the .sort() method
numbers = [4, 2, 7, 1, 9]
print(f"\nOriginal numbers list: {numbers}")

numbers.sort()
print(f"Sorted numbers list: {numbers}")

# List comprehension (cool Python feature)
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares from 1 to 5: {squares}")
