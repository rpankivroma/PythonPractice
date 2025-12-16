"""
Task 5: Password Validator (Intermediate–Advanced)
Description

Write a program that asks the user to enter a password.

Requirements

Use try / except with a custom exception.

Raise an exception if:

The password is shorter than 8 characters

The password contains no digits

Print Password accepted if valid.

Print a clear error message if invalid.
"""

# Answer

class PasswordError(Exception):
    pass


password = input("Enter your password: ")

try:
    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long")

    if not any(char.isdigit() for char in password):
        raise PasswordError("Password must contain at least one digit")

    print("Password accepted")

except PasswordError as e:
    print("Invalid password:", e)

"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 5.py"
Enter your password: 123
Invalid password: Password must be at least 8 characters long
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 5.py"
Enter your password: asdfghjklo
Invalid password: Password must contain at least one digit
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 5.py"
Enter your password: 123456789
Password accepted
PS C:\Users\trade> 
"""