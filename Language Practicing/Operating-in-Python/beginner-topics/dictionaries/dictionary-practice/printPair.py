'''
PROMPT: Write a function print_pair() that takes in a dictionary and a target key.
If the key exists in the dictionary, print the key and its corresponding value.
If the key does not exist, print "That pair does not exist!"

Expected Output:
Key: patrick  
Value: star  
That pair does not exist!  
Key: spongebob  
Value: squarepants
'''

# METHOD 1: Standard version that prints directly (beginner-friendly)
def print_pair(dictionary, target):
    if target in dictionary:
        print("Key:", target)
        print("Value:", dictionary[target])
    else:
        print("That pair does not exist!")


# METHOD 2: Returns the result as a string instead of printing (for flexibility)
def print_pair_return(dictionary, target):
    if target in dictionary:
        return f"Key: {target}\nValue: {dictionary[target]}"
    else:
        return "That pair does not exist!"

if __name__ == '__main__':
    characters = {
        "spongebob": "squarepants",
        "patrick": "star",
        "squidward": "tentacles"
    }

    print("Print Method:")
    print_pair(characters, "patrick")
    print_pair(characters, "plankton")
    print_pair(characters, "spongebob")

    print("\nReturn Method:")
    print(print_pair_return(characters, "patrick"))
    print(print_pair_return(characters, "plankton"))
    print(print_pair_return(characters, "spongebob"))
