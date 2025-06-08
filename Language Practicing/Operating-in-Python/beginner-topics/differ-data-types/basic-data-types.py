# fav_movies
horror = input("What is their favorite horror/thriller movie?: ")
scifi = input("What is their favorite sci-fi movie?: ")
rom = input("What is their favorite romantic movie?: ")
best = input("What is the best movie of all time?: ")

print("Your favorite horror film is:", horror)
print("Your favorite sci-fi film is:", scifi)
print("Your favorite romantic movie is:", rom)
print("Of course the best movie of all time is", best)


# worst_calculator
num1 = int(input("\nEnter a whole number #1: "))
num2 = int(input("Enter one more whole number #2: "))
float1 = float(input("Let's enter decimal #1: "))
float2 = float(input("Let's enter another decimal #2: "))
float3 = float(input("Let's enter one last decimal #3: "))

total_nums = num1 + num2
total_floats = float1 * float2 * float3

print("The sum of the integers", num1, "and", num2, "is", total_nums)
print("Multiplying the floats", str(float1) + ",", float2, "and", float3, "equals", str(total_floats))
