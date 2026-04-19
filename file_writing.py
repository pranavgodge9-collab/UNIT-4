
filename = "source.txt"

with open(filename, "w") as file:
    file.write("This is the first line of the file.\n")
    print(f"1. Successfully wrote initial data to {filename}.")

with open(filename, "r") as file:
    content = file.read()
    print("\n2. Current file content:")
    print(content)

with open(filename, "a") as file:
    file.write("This line was added using append mode.\n")
    print(f"3. Successfully appended new data to {filename}.")

with open(filename, "r") as file:
    updated_content = file.read()
    print("\n4. Updated file content:")
    print(updated_content)

