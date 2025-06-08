# Understanding the basics of if-elif-else statements in Python

# Let's start off by checking a number i.e. legal drinking age
print("You've entered the Jack Daniel's liquor store!")
legal_num = int(input("What is the age on your State ID: "))

if legal_num < 18 :
    print("You can't purchase anything in the store.")
elif legal_num == 18:
    print("Just hit the legal age, shop carefully.")
else:
    print("Enjoy yourself!")

# Next example, let's check the age for a movie rating
movie_age = int(input("\nEnter your age: "))

if movie_age >= 18:
    print("You can watch R-rated movies!")
elif movie_age >= 13:
    print("You can watch PG-13 movies.")
else:
    print("You can watch G-rated movies.")
