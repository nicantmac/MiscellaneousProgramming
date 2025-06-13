# How to define and use nested functions in Python

# --- Basic nested function ---

def outer_function():
    print("I am the outer function!")

    # Define a nested function inside the outer function
    def inner_function():
        print("I am the inner (nested) function!")

    # Call the inner function
    inner_function()

# Call the outer function
outer_function()

# --- Nested function with parameters ---

def greet_person(name):
    print(f"Greeting {name}!")

    def format_message(msg):
        return f"*** {msg} ***"

    # Use the nested function
    formatted = format_message(f"Hello, {name}!")
    print(formatted)

greet_person("Alice")

# --- Returning a nested function (closure pattern) ---

def make_multiplier(factor):
    print(f"Creating a multiplier of {factor}")

    def multiplier(number):
        return number * factor  # factor is remembered!

    return multiplier  # return the inner function

# Create multiplier functions
times3 = make_multiplier(3)
times5 = make_multiplier(5)

# Call the returned functions
print("3 * 10 =", times3(10))
print("5 * 10 =", times5(10))

# --- Summary ---
# - You can define a function inside another function (nested function)
# - The inner function can access variables from the outer function
# - You can return the inner function to create a closure
# - Nested functions are often used to:
#     * Hide helper functions
#     * Implement closures
#     * Build decorators (advanced topic)
