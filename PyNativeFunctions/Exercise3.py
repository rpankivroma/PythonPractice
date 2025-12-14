"""
Exercise 3: Return multiple values from a function
Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.

Given:

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output

50, 30
"""

# Answer:

def calculation(a, b):
    sum = a + b
    sub = a - b
    return sum, sub

res = calculation(40, 10)
print(res)

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise3.py
(50, 30)
"""