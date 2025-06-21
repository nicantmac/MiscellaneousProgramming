def min_distance(words, word1, word2):
    # Step 1: Set a very big number as the starting minimum distance
    smallest_distance = len(words)

    # Step 2: Loop through every word with index
    for i in range(len(words)):
        if words[i] == word1:
            # Now look ahead to find the closest word2
            for j in range(len(words)):
                if words[j] == word2:
                    # Find distance between the positions
                    distance = abs(i - j)
                    # Update smallest distance if this one is smaller
                    if distance < smallest_distance:
                        smallest_distance = distance

    return smallest_distance

if __name__ == '__main__';

words = ["code", "path", "code", "contribute", "practice"]
print(min_distance(words, "code", "practice"))  # → 2
