# Q.47]  Write a Python program to read a random line from a file.

import random

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                return random_line.strip()
            else:
                return "the file is empty"
    except FileNotFoundError:
        return "The file was not found"
    except Exception as e:
        return f"An error occurred: {e}"
    
file_path = 'Th.txt'
print(read_file(file_path))
