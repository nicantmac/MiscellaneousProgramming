# Here we will practice and understand type casting in Python (Type Conversion)

# String to Integer
str_num = "42"
int_num = int(str_num)
print(f"String '{str_num}' as integer: {int_num} (type: {type(int_num)})")

# String to Float
str_float = "3.1415"
float_num = float(str_float)
print(f"String '{str_float}' as float: {float_num} (type: {type(float_num)})")

# Integer to String
age = 25
str_age = str(age)
print(f"Integer {age} as string: '{str_age}' (type: {type(str_age)})")

# Float to String
pi = 3.1415
str_pi = str(pi)
print(f"Float {pi} as string: '{str_pi}' (type: {type(str_pi)})")

# Integer to Float
whole_number = 10
float_number = float(whole_number)
print(f"Integer {whole_number} as float: {float_number} (type: {type(float_number)})")

# Float to Integer (truncates the decimal part!)
decimal_number = 9.99
int_number = int(decimal_number)
print(f"Float {decimal_number} as integer: {int_number} (type: {type(int_number)})")

# String to Boolean
str_value = "hello"
bool_value = bool(str_value)  # non-empty string = True
print(f"String '{str_value}' as boolean: {bool_value} (type: {type(bool_value)})")

# Example with empty string:
empty_str = ""
bool_empty = bool(empty_str)  # empty string = False
print(f"Empty string as boolean: {bool_empty} (type: {type(bool_empty)})")
