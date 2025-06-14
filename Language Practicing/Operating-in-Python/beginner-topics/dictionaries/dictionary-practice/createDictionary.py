def create_dictionary(keys, values):
    new_dict = {}  # Start with an empty dictionary

    for i in range(len(keys)):  # Loop over the indices of the keys/values lists
        key = keys[i]           # Get the key at the current index
        value = values[i]       # Get the corresponding value at the same index
        new_dict[key] = value   # Add the key-value pair to the dictionary

    return new_dict             # Return the completed dictionary



def create_dictionary(keys, values):
    return dict(zip(keys, values))

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

print(create_dictionary(keys, values))
