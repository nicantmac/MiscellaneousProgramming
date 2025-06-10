# data-type-methods.py
# Demonstrating methods of common Python data types

# String methods
s = "hello world"

print("\nString methods:")
print("upper():", s.upper())
print("capitalize():", s.capitalize())
print("replace():", s.replace("world", "Python"))
print("split():", s.split())

# List methods
lst = [3, 1, 4, 1, 5]

print("\nList methods:")
lst.append(9)
print("append(9):", lst)

lst.sort()
print("sort():", lst)

lst.reverse()
print("reverse():", lst)

print("count(1):", lst.count(1))

# Dictionary methods
inventory = {"json": "data", "AWS": "cloud-computing", "Microsoft": "Windows 10"}

print("\nDictionary methods:")
print("keys():", inventory.keys())  # #This returns a view of all the key in the dictionary as a list
print("values():", inventory.values())  #This returns a view of all the values in the dictionary as a list
print("items():", inventory.items())  # This returns a view of all the key-value pairs as tuples

# Set methods
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("\nSet methods:")
print("union():", s1.union(s2))
print("intersection():", s1.intersection(s2))
print("difference():", s1.difference(s2))
