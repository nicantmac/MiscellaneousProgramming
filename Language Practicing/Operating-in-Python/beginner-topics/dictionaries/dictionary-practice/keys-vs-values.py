'''
PROMPT: Write a function keys_v_values() that takes in a dictionary with integer keys and integer values.
The function should compare the sum of the keys and the sum of the values and return:
- "keys" if the sum of the keys is greater,
- "values" if the sum of the values is greater,
- "balanced" if they are equal.

Expected Output:
- For {1:10, 2:20, 3:30, 4:40, 5:50, 6:60} → "values"
- For {100:10, 200:20, 300:30, 400:40, 500:50, 600:60} → "keys"
'''

# METHOD 1: Standard approach using sum() and if-else comparison
def keys_v_values_manual(dictionary):
    sum_keys = sum(dictionary.keys())      # Sum all keys
    sum_values = sum(dictionary.values())  # Sum all values

    if sum_keys > sum_values:
        return "keys"
    elif sum_values > sum_keys:
        return "values"
    else:
        return "balanced"


# METHOD 2: Slightly cleaner one-liner with max()
def keys_v_values_efficient(dictionary):
    sums = {
        "keys": sum(dictionary.keys()),
        "values": sum(dictionary.values())
    }
    if sums["keys"] == sums["values"]:
        return "balanced"
    return max(sums, key=sums.get)  # Return "keys" or "values" based on which has the higher sum


if __name__ == '__main__':
    dict1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
    dict2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}

    print("Manual Method:")
    print(keys_v_values_manual(dict1))  # Output: values
    print(keys_v_values_manual(dict2))  # Output: keys

    print("\nEfficient Method:")
    print(keys_v_values_efficient(dict1))  # Output: values
    print(keys_v_values_efficient(dict2))  # Output: keys
