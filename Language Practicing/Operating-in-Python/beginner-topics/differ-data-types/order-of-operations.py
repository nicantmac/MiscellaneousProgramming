# Operator Precedence in Python (Order of Operations)

# Simple Example
result1 = 3 + 4 * 2
# Expected: 3 + (4 * 2) = 3 + 8 = 11
print(f"3 + 4 * 2 = {result1}")

# Using Parentheses to Change Order
result2 = (3 + 4) * 2
# Expected: (3 + 4) * 2 = 7 * 2 = 14
print(f"(3 + 4) * 2 = {result2}")

# Exponents come before multiplication
result3 = 2 + 3 ** 2 * 2
# Expected: 2 + (3 ** 2) * 2 = 2 + 9 * 2 = 2 + 18 = 20
print(f"2 + 3 ** 2 * 2 = {result3}")

# Division and Multiplication are evaluated left to right
result4 = 100 / 5 * 2
# Expected: (100 / 5) * 2 = 20 * 2 = 40.0
print(f"100 / 5 * 2 = {result4}")

# Full Example: Mixed Operators
result5 = (5 + 3) * (12 / 4) - 6 ** 2 + 10
# Step by step:
# (5 + 3) = 8
# (12 / 4) = 3
# 6 ** 2 = 36
# So: 8 * 3 - 36 + 10 → 24 - 36 + 10 → -12 + 10 → -2
print(f"(5 + 3) * (12 / 4) - 6 ** 2 + 10 = {result5}")

# ----------------------------------------
# Summary of Precedence (PEMDAS):
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication * and Division / (left to right)
# 4. Addition + and Subtraction - (left to right)
# ----------------------------------------
