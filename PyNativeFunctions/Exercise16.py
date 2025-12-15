"""
Exercise 16: Use a lambda with the map() function to double each element in a list
Given:

numbers = [1, 2, 3, 4, 5]
Expected Output:

The doubled numbers are: [2, 4, 6, 8, 10]
"""

# Answer

numbers = [1, 2, 3, 4, 5]

DoubledNumbers = list(map(lambda x: x * 2, numbers))
print("The doubled numbers are:", DoubledNumbers)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise16.py
The doubled numbers are: [2, 4, 6, 8, 10]
"""