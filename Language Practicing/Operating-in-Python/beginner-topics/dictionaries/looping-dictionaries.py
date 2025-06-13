# Here is a simple dictionary where we will manipulate it in different ways by looping
my_dict = {"name": "Eve", "age": 22, "city": "Chicago"}

# Using the 'in' keyword, here we simply loop through the keys
print("\nKeys:")
for key in my_dict:
    print(key) 

# To loop through the values, use the .values() method to retrieve the values
print("\nValues:")
for value in my_dict.values():
    print(value)

# To retrieve both keys-values, loop through the key-value pairs using the .items() method
print("\nKey-Value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
    
