# Open the file in write mode and write content to it
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("We will perform various file operations on this file.\n")

# Open the file in read mode and read its content
with open("sample.txt", "r") as file:
    # Read the first 10 characters
    content = file.read(10)
    print("First 10 characters:")
    print(content)

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read the entire content of the file
    content = file.read()
    print("\nEntire content of the file:")
    print(content)

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read the file line by line using a for loop
    print("\nReading the file line by line:")
    for line in file:
        print(line.strip())

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read the first line using readline()
    line1 = file.readline()
    print("\nFirst line:")
    print(line1.strip())

    # Read the second line using readline()
    line2 = file.readline()
    print("Second line:")
    print(line2.strip())

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Read all lines using readlines()
    lines = file.readlines()
    print("\nAll lines as a list:")
    print(lines)

    # Get the current position of the file pointer
    position = file.tell()
    print("\nCurrent position of the file pointer:", position)

# Open the file in append mode and append content to it
with open("sample.txt", "a") as file:
    file.write("\nThis line is appended to the file.")

# Open the file in read mode and read the updated content
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nUpdated content of the file:")
    print(content)