# Write a program to read the content of file
# line by line and write it to another file except
# for the lines containing "a" letter in it.
    
# Function to copy lines except those containing 'a'
def filter_lines_without_a(source_file_path, output_file_path):
    try:
        with open(source_file_path, 'r') as source_file, open(output_file_path, 'w') as output_file:
            for line in source_file:
                if 'a' not in line:
                    output_file.write(line)
    except FileNotFoundError:
        print(f"The file {source_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_path = 'source.txt'
output_path = 'output.txt'
filter_lines_without_a(source_path, output_path)

print(f"Lines from {source_path} have been copied to {output_path}, excluding lines containing 'a'.")
