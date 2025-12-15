"""
Exercise 15: Use a lambda with the filter() function to get all even numbers from a list
Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected Output:

The even numbers in the list are: [2, 4, 6, 8, 10]
"""

# Answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers in the list are: {even_numbers}")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise15.py
The even numbers in the list are: [2, 4, 6, 8, 10]
"""