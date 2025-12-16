"""
Request: Give me one practice task on topic Python Casting 
based on https://www.w3schools.com/python/python_casting.asp

GPT Task: Practice Type Casting
Write a Python program that:
1. Creates three variables:
    - a with the string value "5"
    - b with the float value 4.7
    - c with the integer value 8
2. Convert and print the results of:
    - a converted to an integer and added to c
    - b converted to an integer
    - c converted to a float
    - c converted to a string and combined with " is a number"
3. Print the data type of each converted variable using the type() function.
"""

#Answer:
x = 5
y = 4.7
z = 8


a = str(x)
b = float(y)
c = int(z)

a = int(x)
print(a + c)
b = int(y)
print(b)
c1 = float(z)
print(c)
c = str(z)
print(c, "is a number")

print(type(a))
print(type(b))
print(type(c1))
print(type(c))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/Part1/PythonCasting.py
13
4
8
8 is a number
<class 'int'>
<class 'int'>
<class 'float'>
<class 'str'>
"""