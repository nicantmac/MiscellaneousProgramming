# How to handle errors in Python using try, except, else, finally

# --- Basic try-except ---

try:
    print("Dividing 10 by 2...")
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

# --- Handling a specific error ---

try:
    print("\nDividing 10 by 0...")
    result = 10 / 0
except ZeroDivisionError:
    print("❌ ZeroDivisionError caught!")

# --- Handling multiple types of errors ---

try:
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except IndexError:
    print("❌ IndexError caught!")
except ValueError:
    print("❌ ValueError caught!")

# --- Catch-all (generic Exception) ---

try:
    value = int("hello")  # ValueError
except Exception as e:
    print("❌ An error occurred:", e)

# --- Using else with try-except ---

try:
    print("\nTrying division...")
    result = 10 / 5
except ZeroDivisionError:
    print("❌ Division failed!")
else:
    print("✅ Division successful, result:", result)

# --- Using finally (always runs) ---

try:
    print("\nTrying risky operation...")
    result = 10 / 1
except ZeroDivisionError:
    print("❌ Division failed!")
finally:
    print("✨ Finally block: This always runs!")

# --- Raising your own exceptions ---

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print(f"Age is valid: {age}")

try:
    check_age(-5)
except ValueError as e:
    print("❌ Custom ValueError caught:", e)

# --- Summary ---
# - Use try/except to handle errors
# - Catch specific errors first
# - else block runs if no error occurs
# - finally block always runs (good for cleanup)
# - You can raise your own exceptions with raise
