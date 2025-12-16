"""
Task 4: File Reader (Intermediate)
Description

Create a program that tries to open and read a text file.

Requirements

Use try / except to handle FileNotFoundError.

If the file exists, print its contents.

If it does not exist, print:
File not found.
"""

# Answer

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found.")

