"""
Exercise 6: Create a recursive function
Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

A recursive function is a function that calls itself repeatedly.

Expected Output:
55
"""
# Answer

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise6.py
55
"""