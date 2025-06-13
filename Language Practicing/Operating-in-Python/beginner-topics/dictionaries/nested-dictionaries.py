# Here is practice with nested dictionaries
# The dictionary below is what's going to be manipulated
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

# Here is how to access nested values in a dictionary
print("Student1 name:", students["student1"]["name"])  # Output: Student1 name: Alice
print("Student2 major:", students["student2"]["major"])  # Output: Student2 major: Math


# How to loop through nested dictionary
# student_id = student1 & student2, the student_info = the keys-values within student1 & student2
for student_id, student_info in students.items():
    print(f"\n{student_id}:")  # Outputs: student1 & student2
    for key, value in student_info.items():
        print(f"  {key}: {value}")  # Outputs students keys-values 
