'''
PROMPT: Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. 
The function returns a dictionary where each item in keys is paired with a corresponding item in values.

Expected Output: {"peanut": "butter", "dragon": "fly", "star": "fish", "pop": "corn", "space": "ship"}
'''

# Here our function will be able to take both list; keys & values
def create_dictionary_manual(keys, values):
    new_dict = {}  # let's create a empty dictionary we want filled
    
    for i in range(len(keys)):  # lets 'for-loop' over the indices of the keys list
        key = keys[i]  # get the current index in keys list
        value = values[i]  # get the current index in values list
        new_dict[key] = value  # Using dict[key] = val format, this will add the key-value pairs to the dictionary

    return new_dict  # when all done, return the completed dictionary


# More efficient method
def create_dictionary_zip(keys, values):
    new_dict = zip(keys, values)  # .zip() creates tuple pairs i.e. -> ('peanut', 'dragon'), ('star', 'pop')...
    return dict(new_dict)  # dict() creates a dictionary of the two values respectively

if __name__ == '__main__':
    keys = ["peanut", "dragon", "star", "pop", "space"]
    values = ["butter", "fly", "fish", "corn", "ship"]
    
    print(create_dictionary_manual(keys, values))
    print(create_dictionary_zip(keys, values))
