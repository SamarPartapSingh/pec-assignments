import os
import random
import string

# Directory where you want to create the text files
output_directory = "python_3"

# Number of text files to create
num_files = 500

# Number of lines per file
num_lines = 20000

# Length of each line (number of characters)
line_length = 20

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Generate and write the text files
for i in range(1, num_files + 1):
    filename = os.path.join(output_directory, f"file_{i}.txt")
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_line = ''.join(random.choice(string.ascii_letters) for _ in range(line_length))
            file.write(random_line + '\n')

print(f'{num_files} text files with {num_lines} lines each, containing {line_length}-character strings, have been created in {output_directory}.')
