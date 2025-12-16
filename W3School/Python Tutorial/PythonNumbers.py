"""
Request: Give me one practice task on topic Python Numbers 
based on https://www.w3schools.com/python/python_numbers.asp

GPT Task: Work with Python Numbers
Write a Python program that:

1. Creates three variables:
    - x as an integer
    - y as a float
    - z as a complex number
2. Prints each variable and its data type using the type() function.
3. Converts:
    - x to a float
    - y to an integer
    - z to a string
    Then print each converted value and its new type.
4. Use the random module to print a random number between 1 and 50.
"""
#Answer:

import random

x = int()
y = float()
z = complex()

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = float()
y = int()
z = str()

print(x, type(x))
print(y, type(y))
print(z, type(z))

print("Random number between 1 and 50:", random.randrange(1, 50))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/Part1/PythonNumbers.py
0 <class 'int'>
0.0 <class 'float'>
0j <class 'complex'>
0.0 <class 'float'>
0 <class 'int'>
 <class 'str'>
Random number between 1 and 50: 22
"""