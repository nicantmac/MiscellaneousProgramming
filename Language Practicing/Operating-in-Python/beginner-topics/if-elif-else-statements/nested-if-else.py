# Here will understand and practice nesting if-else statements

# Let's understand our college journey with a nested if-else statement choosing a STEM field

print("=== STEM Major Advisor ===")
field = input("Which STEM field are you interested in? (engineering / science / technology / mathematics): ").lower()

if field == "engineering":
    branch = input("Which branch? (mechanical / electrical / civil / chemical): ").lower()

    if branch == "mechanical":
        print("Mechanical Engineering: Great choice for designing machines and working with robotics!")
    elif branch == "electrical":
        print("Electrical Engineering: You'll master circuits, power systems, and electronics.")
    elif branch == "civil":
        print("Civil Engineering: Shape the world by building infrastructure!")
    elif branch == "chemical":
        print("Chemical Engineering: Work with processes and materials in industries.")
    else:
        print("That engineering branch is not in our system.")

elif field == "science":
    science_branch = input("Which science? (physics / biology / chemistry / earth): ").lower()

    if science_branch == "physics":
        print("Physics: Explore the fundamental laws of the universe!")
    elif science_branch == "biology":
        print("Biology: Study life, from cells to ecosystems.")
    elif science_branch == "chemistry":
        print("Chemistry: Experiment with materials and reactions.")
    elif science_branch == "earth":
        print("Earth Science: Learn about the Earth, its history, and its systems.")
    else:
        print("That science branch is not in our system.")

elif field == "technology":
    tech_branch = input("Which area? (computer science / information systems / cybersecurity / AI): ").lower()

    if tech_branch == "computer science":
        print("Computer Science: Software, algorithms, and problem solving — the core of modern tech.")
    elif tech_branch == "information systems":
        print("Information Systems: Manage technology and data to solve business problems.")
    elif tech_branch == "cybersecurity":
        print("Cybersecurity: Protect systems from digital threats — a critical, fast-growing field.")
    elif tech_branch == "ai":
        print("AI (Artificial Intelligence): Build intelligent systems to transform industries.")
    else:
        print("That technology branch is not in our system.")

elif field == "mathematics":
    print("Mathematics: The language of science, great foundation for any STEM path!")

else:
    print("That is not a recognized STEM field. Please choose engineering, science, technology, or mathematics.")
