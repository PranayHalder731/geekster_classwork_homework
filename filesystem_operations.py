import os
import shutil

# Define directory and file names
new_directory = "new_folder"
file_name = "example.txt"
new_file_name = "renamed_example.txt"

# 1. Create a new directory
os.makedirs(new_directory, exist_ok=True)
print(f"Directory '{new_directory}' created.")

# 2. List all files and directories in the current working directory
print("\nCurrent directory contents:")
print(os.listdir("."))

# 3. Create a new text file in the new directory and write content to it
file_path = os.path.join(new_directory, file_name)
with open(file_path, "w") as file:
    file.write("Hello, this is a sample text file.")
print(f"\nFile '{file_name}' created and content written.")

# 4. Read the content of the newly created text file
with open(file_path, "r") as file:
    content = file.read()
print(f"\nContent of '{file_name}': {content}")

# 5. Rename the text file
new_file_path = os.path.join(new_directory, new_file_name)
os.rename(file_path, new_file_path)
print(f"\nFile '{file_name}' renamed to '{new_file_name}'.")

# 6. List all files and directories in the new directory after renaming the file
print(f"\nContents of '{new_directory}' after renaming:")
print(os.listdir(new_directory))

# 7. Delete the new directory and its contents
shutil.rmtree(new_directory)
print(f"\nDirectory '{new_directory}' and its contents deleted.")
