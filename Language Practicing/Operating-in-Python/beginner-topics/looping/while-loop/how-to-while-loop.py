# Here you will understand while-looping in Python and obtain a strong foundation

# ----- Notes/Reminders -----
# A while loop will keep looping ***as long as the condition is True***.
# If the condition becomes False, the looping will stop.
# You must make sure the condition eventually becomes False → or you'll create an infinite loop!

# Here we start off with basic while looping
print("Counting from 1 to 5 using while loop:")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # If you forget this line, you'll encounter an infinite loop.

# Let's practice while looping to validate a user's input
print("\nEnter a positive number (loop will stop when you do):")
number = -1
while number <= 0:
    number = int(input("Enter a positive number: "))

print(f"You entered: {number} — good job!")

# Infinite loop with break
print("\nWhile loop with break (loop until user types 'exit'):")

while True:  # Infinite loop — will only stop when 'break' is called
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == "exit":
        print("Exiting loop.")
        break  # Immediately exit the while loop
    else:
        print(f"You typed: {user_input}")

# While loop with else -----
print("\nCounting with while + else:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop ended naturally — condition is now False.")

# Note: The 'else' in a while loop runs only if the loop **did not exit by break**.
