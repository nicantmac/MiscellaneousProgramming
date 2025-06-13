# tuples_builtins.py
# Useful built-in functions with tuples

my_tuple = (10, 20, 30, 40, 50)

# len() → number of elements
print("Length of tuple:", len(my_tuple))

# sum() → sum of elements (if all elements are numeric)
print("Sum of tuple:", sum(my_tuple))

# max() → largest element
print("Max of tuple:", max(my_tuple))

# min() → smallest element
print("Min of tuple:", min(my_tuple))

# tuple() → convert another iterable to a tuple
my_list = [100, 200, 300]
converted = tuple(my_list)
print("Converted list to tuple:", converted)

# sorted() → returns a sorted list (does NOT modify the tuple)
sorted_list = sorted(my_tuple)
print("Sorted version of tuple (as list):", sorted_list)

# in operator → test membership
print("Is 20 in the tuple?", 20 in my_tuple)

# Loop through tuple
print("Looping through tuple:")
for item in my_tuple:
    print(item)
