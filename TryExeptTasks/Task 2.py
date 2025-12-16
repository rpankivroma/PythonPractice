"""
Task 2: Division Calculator (Beginner–Intermediate)
Description

Create a program that divides two numbers entered by the user.

Requirements

Use try / except to handle:

ZeroDivisionError

ValueError

If division is successful, print the result.

If an error occurs, print an appropriate message.
"""

# Answer

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = a / b
    print("Your result is", result)
    
except ZeroDivisionError:
    print("You can't devide by zero")

except ValueError:
    print("Plase enter a number")

"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 2.py"
Enter the first number: 2
Enter the second number: 2
Your result is 1.0
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 2.py"
Enter the first number: 2
Enter the second number: 0
You can't devide by zero
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 2.py"
Enter the first number: 2
Enter the second number: sd
Plase enter a number
"""