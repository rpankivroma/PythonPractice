"""
Exercise 5: Create an inner function
Create a program with nested functions to perform an addition calculation as follows:

Define an outer function that accepts two parameters, a and b.
Inside this outer function, define an inner function that calculates the sum of a and b.
The outer function should then add 5 to this sum.
Finally, the outer function should return the resulting value.”
"""

# Answer: 

def outer_fun(a, b):
    square = a ** 2

    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5

result = outer_fun(5, 10)
print(result)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise5.py
20
"""