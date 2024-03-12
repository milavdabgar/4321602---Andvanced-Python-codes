# Read the file name from the user
file_name = input("Enter a file name: ")

# Initialize an empty set to store unique words
unique_words = set()

try:
    # Open the file for reading
    with open(file_name, 'r') as file:
        # Read the file line by line
        for line in file:
            # Split the line into words
            words = line.strip().split()
            
            # Add the words to the set of unique words
            unique_words.update(words)

    # Convert the set to a sorted list
    sorted_words = sorted(list(unique_words))

    # Print the sorted list of unique words
    print(sorted_words)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")