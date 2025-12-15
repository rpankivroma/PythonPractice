"""
Exercise 13: Write a recursive function to calculate the factorial
Write a recursive function to calculate the factorial of a non-negative integer.
"""

# Answer

def FactorialFunk(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1  
    else:
        return n * FactorialFunk(n - 1) 

# Example usage:
number = 5
result = FactorialFunk(number)
print(f"The factorial of {number} is {result}") 

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise13.py
The factorial of 5 is 120
"""