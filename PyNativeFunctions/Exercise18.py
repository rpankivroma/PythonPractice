"""
Exercise 18: Create Higher-Order Function
Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, 
and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).

The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.
"""

# Answer

def apply_operation(func, x, y):
    return func(x,y)


def add(a, b):
  return a + b

result_add = apply_operation(add, 5, 3)
print(f"Result of addition: {result_add}")

# Demonstrate with subtraction using a lambda function
subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f"Result of subtraction: {result_subtract}")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise18.py
Result of addition: 8
Result of subtraction: 6
"""
