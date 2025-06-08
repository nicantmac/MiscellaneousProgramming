# Here you will understand; Strings (str), Integers (int), Floats (float), Booleans (bool)

# Strings with user-input
horror = input("What is their favorite horror/thriller movie?: ")
best = input("What is the best movie of all time?: ")

print("Your favorite horror film is: ", horror)
print("Of course the best movie of all time is: ", best)

# Here let's create a quasi calculator that's able to calculate Ints and Floats

# Integers
num1 = int(input("\nEnter a whole number #1: "))
num2 = int(input("Enter one more whole number #2: "))
total_nums = num1 + num2
print("The sum of the integers ", num1, " and ", num2, " is ", total_nums)

# Floats
float1 = float(input("Enter decimal number #1: "))
float2 = float(input("Enter decimal number #2: "))
float3 = float(input("Enter decimal number #3: "))
total_floats = float1 * float2 * float3
print("Multiplying the floats: ", float1 + ", ", float2, " and ", float3, " equals ", total_floats)

# Booleans
likes_movies = True
likes_cardio = False
print(f"\nDo you like movies? Answer: {likes_movies}")
print(f"\nDo you like cardio? Answer: {likes_cardio}")
