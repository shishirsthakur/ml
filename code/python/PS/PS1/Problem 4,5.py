import os

# Specify the directory path (use '.' for the current directory)
path = 'Problem 4'

# Get the list of all files and directories
contents = os.listdir(path)

# Print the contents
print("Directory contents:")
for item in contents:
    print(item)
