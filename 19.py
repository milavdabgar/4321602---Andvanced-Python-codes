import pickle

def create_binary_file():
    """Creates a binary file to store roll numbers and names."""
    student_records = {}
    with open('students.dat', 'wb') as file:
        while True:
            roll_no = int(input("Enter Roll Number (or 0 to stop): "))
            if roll_no == 0:
                break
            name = input("Enter Name: ")
            student_records[roll_no] = name
            pickle.dump(student_records, file)

def search_roll_no():
    """Searches for a roll number in the binary file."""
    with open('students.dat', 'rb') as file:
        student_records = {}  # Initialize an empty dictionary
        try:
            while True:
                # Load all records into the dictionary
                student_records.update(pickle.load(file))
        except EOFError:
            pass  # Exit loop when end of file is reached

        roll_no = int(input("Enter Roll Number to search: "))
        if roll_no in student_records:
            print("## Name is :", student_records[roll_no], "##")
        else:
            print("## Rollno not found ##")


# Create the binary file (uncomment if needed)
# create_binary_file()

# Search for roll numbers
search_roll_no()
