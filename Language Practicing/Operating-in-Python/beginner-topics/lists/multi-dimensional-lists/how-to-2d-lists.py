# how-to-multidim-lists.py
# ----------------------------------------
# Multi-Dimensional Lists in Python
# AKA "Lists inside of lists"
# ----------------------------------------

# 1️⃣ 2D List (List of Lists)

matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(f"Top left: {matrix_2d[0][0]}")       # 1
print(f"Middle: {matrix_2d[1][1]}")         # 5
print(f"Bottom right: {matrix_2d[2][2]}")   # 9

# Looping through 2D list
print("\nLooping through 2D matrix:")
for row in matrix_2d:
    for val in row:
        print(val, end=" ")
    print()

# 2️⃣ Modifying elements in a 2D list
matrix_2d[0][0] = 100
print(f"\nAfter modification: {matrix_2d[0][0]}")  # 100

# ----------------------------------------

# 3️⃣ 3D List (List of List of Lists)

cube_3d = [
    [  # Layer 0
        [1, 2],
        [3, 4]
    ],
    [  # Layer 1
        [5, 6],
        [7, 8]
    ]
]

# Accessing elements in 3D
print(f"\nElement at Layer 0, Row 1, Col 1: {cube_3d[0][1][1]}")  # 4
print(f"Element at Layer 1, Row 0, Col 0: {cube_3d[1][0][0]}")  # 5

# Looping through 3D list
print("\nLooping through 3D cube:")
for layer in cube_3d:
    for row in layer:
        for val in row:
            print(val, end=" ")
        print()
    print("--- End of Layer ---")

# ----------------------------------------

# 4️⃣ Creating empty 2D list (e.g. 3 rows x 4 cols filled with 0s)

rows = 3
cols = 4
empty_2d = [[0 for _ in range(cols)] for _ in range(rows)]

print(f"\n3x4 Zero Matrix: {empty_2d}")
