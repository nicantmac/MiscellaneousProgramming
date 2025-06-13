# How to define and use functions in Python

# --- Basic Function ---

# Define a function
def greet():
    print("Hello!")

# Call the function
greet()

# --- Function with parameters ---

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# --- Function with return value ---

def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)

# --- Function with default parameter ---

def greet_with_default(name="friend"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Bob")

# --- Function with multiple return values (tuple) ---

def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

nums = [4, 2, 8, 6]
min_val, max_val, total = get_stats(nums)
print(f"Min: {min_val}, Max: {max_val}, Sum: {total}")

# --- Keyword arguments ---

def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

print_info(age=25, city="NYC", name="Alice")  # keyword arguments can be out of order

# --- Variable number of arguments (*args) ---

def print_args(*args):
    print("Arguments:", args)

print_args(1, 2, 3, "hello")

# --- Variable number of keyword arguments (**kwargs) ---

def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)

print_kwargs(name="Alice", age=25, city="NYC")

# --- Lambda functions (anonymous functions) ---

square = lambda x: x * x
print("Square of 5:", square(5))

# --- Summary ---

# ✅ Define a function with def
# ✅ Functions can return values
# ✅ Parameters can have default values
# ✅ Can use *args and **kwargs for flexible arguments
# ✅ Lambda → simple anonymous function
