"""
Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
Given:
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
Expected Output:
The sorted list of tuples based on the second element is: [('date', 1), ('banana', 2), ('apple', 5), ('cherry', 8)]
"""

# Answer

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

SortedList = sorted(data, key=lambda item: item[1])
print("The sorted list of tuples based on the second element is:", SortedList)

"""
Terminal Output: 
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise17.py
The sorted list of tuples based on the second element is: [('date', 1), ('banana', 2), ('apple', 5), ('cherry', 8)]
"""