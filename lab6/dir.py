#1
import os

def list_contents(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All Contents:", os.listdir(path))

#2
import os

def check_access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")
    
#3
import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist.")
    
#4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

#5 
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

generate_files()

#7
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())
        
#8
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} has been deleted.")
        else:
            print(f"Cannot delete {path}: No write permission.")
    else:
        print(f"File {path} does not exist.")
