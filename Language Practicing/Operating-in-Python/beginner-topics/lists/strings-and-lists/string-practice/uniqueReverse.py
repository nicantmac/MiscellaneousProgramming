def reverse_only_letters(s):
    letters = [c for c in s if c.isalpha()]
    result = []

    for char in s:
        if char.isalpha():
            result.append(letters.pop())  # reverse using pop from end
        else:
            result.append(char)

    return ''.join(result)

if __name__ == '__main__':
    s = "a-bC-dEf-ghIj"
    reversed_s = reverse_only_letters(s)
    print(reversed_s)
    # Output: "j-Ih-gfE-dCba"
