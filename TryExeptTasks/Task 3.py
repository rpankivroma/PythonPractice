"""
Task 3: List Index Access (Intermediate)
Description

Write a program that asks the user for an index and prints the element from a list.

items = ["apple", "banana", "cherry"]

Requirements

Catch IndexError if the index is out of range.

Catch ValueError if the input is not an integer.

Print a success message if the element is found.
"""

# Answer

items = ["apple", "banana", "cherry"]

try:
    index = int(input("enter index of searched element: "))
    print("The element had been founded:", items[index])
except IndexError:
    print("We haven't got any element with this index. Plase enter the number from 0 to 2")
except ValueError:
    print("Enter a number")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 3.py"
enter index of searched element: 0
The element had been founded: apple
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 3.py"
enter index of searched element: 4
We haven't got any element with this index. Plase enter the number from 0 to 2
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/trade/Desktop/PythonPractice/PythonPractice/TryExeptTasks/Task 3.py"
enter index of searched element: aa
Enter a number
"""