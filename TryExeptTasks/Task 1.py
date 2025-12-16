"""
🐍 Task 1: Safe Number Input (Beginner)
Description

Write a program that asks the user to enter a number.

Requirements

Use try / except to catch a ValueError.

If the input is not a number, print:
Invalid input. Please enter a number.

If the input is valid, print:
You entered: X
"""

# Answer

try:
    x = int(input("Enter your number"))
    print("You entered: ", x)
except ValueError:
    print("Invalid input. Please enter a number.")

"""
Terminal otput
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 1.py"
Enter your number3
You entered:  3
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 1.py"
Enter your numberdd
Invalid input. Please enter a number.
"""