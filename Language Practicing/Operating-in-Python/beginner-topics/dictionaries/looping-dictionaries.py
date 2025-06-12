# Looping through a dictionary

my_dict = {
    "name": "Eve",
    "age": 22,
    "city": "Chicago"
}

# Loop through keys
print("\nKeys:")
for key in my_dict:
    print(key)

# Loop through values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Loop through key-value pairs
print("\nKey-Value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
    
