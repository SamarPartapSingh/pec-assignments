import os
import random
import string
import time
import csv

output_directory = "python 4"

num_files = 500

num_lines = 20000

line_length = 20

os.makedirs(output_directory, exist_ok=True)

results_file = "conversion_results.csv"

results_data = []

for i in range(1, num_files + 1):
    filename = os.path.join(output_directory, f"file_{i}.txt")
    
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_line = ''.join(random.choice(string.ascii_letters) for _ in range(line_length))
            file.write(random_line + '\n')
    
    start_time = time.time()
    with open(filename, 'r') as file:
        data = file.read()
        data_upper = data.upper()
    with open(filename, 'w') as file:
        file.write(data_upper)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    if i % 100 == 0:
        results_data.append((i, elapsed_time))
        accumulated_time = 0 

with open(results_file, 'w', newline='') as csvfile:
    fieldnames = ["No. of Files", "Time Taken (sec)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    accumulated_time = 0
    for i, elapsed_time in results_data:
        accumulated_time += elapsed_time
        writer.writerow({"No. of Files": i, "Time Taken (sec)": accumulated_time})

print(f'Results have been saved in {results_file}.')

