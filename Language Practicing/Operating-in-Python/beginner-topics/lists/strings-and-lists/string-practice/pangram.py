def is_pan(pan_word):
    pan_word = pan_word.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in pan_word:
            return False
    return True

print(is_pan("Hello world"))
print(is_pan("The quick brown fox jumps over the lazy dog"))
