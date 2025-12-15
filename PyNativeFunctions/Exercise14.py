"""
Exercise 14: Create a lambda function that squares a given number
A lambda function in Python is a small anonymous function defined using the lambda keyword. 
The syntax is lambda arguments: expression. The expression is evaluated and returned.
"""

# Answer

x = lambda a: a ** 2

number = 5
squared_number = x(number)
print(f"The square of {number} is {squared_number}")

"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise14.py
The square of 5 is 25
"""