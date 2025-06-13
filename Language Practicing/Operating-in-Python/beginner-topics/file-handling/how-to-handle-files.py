# Basic Python File Handling: Read, Write, Append, with examples

# --- Writing to a file ---
# 'w' mode = write (overwrites file or creates it if it doesn't exist)
with open("demo.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new file.\n")

print("✅ File written using 'w' mode.")

# --- Reading from a file ---
# 'r' mode = read
with open("demo.txt", "r") as file:
    content = file.read()
    print("\n📖 Contents of demo.txt:\n", content)

# --- Reading line by line ---
with open("demo.txt", "r") as file:
    print("📖 Reading line by line:")
    for line in file:
        print(line.strip())  # .strip() removes newline characters

# --- Appending to a file ---
# 'a' mode = append (adds content to the end)
with open("demo.txt", "a") as file:
    file.write("Adding a third line.\n")

print("\n✅ Line appended using 'a' mode.")

# --- Reading lines into a list ---
with open("demo.txt", "r") as file:
    lines = file.readlines()
    print("📄 Lines as list:", lines)

# --- Using try-except to catch file errors ---
try:
    with open("missing_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("❌ FileNotFoundError: 'missing_file.txt' does not exist.")

# --- Writing a list to a file ---
lines_to_write = ["First line\n", "Second line\n", "Third line\n"]
with open("list_output.txt", "w") as file:
    file.writelines(lines_to_write)

print("✅ Wrote list of lines to list_output.txt")

# --- Summary ---
# Modes: 'r' = read, 'w' = write, 'a' = append, 'x' = create
# Always use `with open(...) as` to auto-close files
# read() → entire content
# readline() → one line
# readlines() → list of all lines
# write() / writelines() → write to file
