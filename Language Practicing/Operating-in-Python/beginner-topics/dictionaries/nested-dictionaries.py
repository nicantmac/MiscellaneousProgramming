# dict_nested.py
# Working with nested dictionaries

students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "major": "CS"
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "major": "Math"
    }
}

# Access nested values
print("Student1 name:", students["student1"]["name"])
print("Student2 major:", students["student2"]["major"])

# Loop through nested dict
for student_id, student_info in students.items():
    print(f"\n{student_id}:")
    for key, value in student_info.items():
        print(f"  {key}: {value}")
