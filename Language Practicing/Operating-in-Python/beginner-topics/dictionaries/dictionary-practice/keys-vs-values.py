def keys_v_values(dictionary):
    sum_keys = sum(dictionary.keys())
    sum_values = sum(dictionary.values())

    if sum_keys > sum_values:
        return "keys"
    elif sum_values > sum_keys:
        return "values"
    else:
        return "balanced"


dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print(keys_v_values(dictionary1))  # Output: values

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
print(keys_v_values(dictionary2))  # Output: keys
