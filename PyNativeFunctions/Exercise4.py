"""
Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() with the following specifications:

It should accept the employee’s name and salary.
It should display both the name and salary.
If the salary is not provided in the function call, it should default to 9000.

Home » Python Exercises » Python Functions Exercise
Python Functions Exercise
Updated on: May 22, 2025 | 163 Comments

A Python function is a block of code or a group of statements designed to perform a specific task. Functions are valuable for code reusability, allowing you to execute the same logic whenever needed without writing it multiple times.

This exercise on Python functions aims to help developers learn and practice defining functions, function calls, function arguments, inner functions, and built-in functions. Let us know in the comment section below if you have any alternative solutions. It will help other developers.

Also Read:

Python Functions Quiz
Python functions and Python function arguments to solve questions
Python Functions and Modules Interview Questions
This exercise includes the following: –

It contains Python function assignments, programs, questions, and challenges.
Total 18 questions. The solution is provided for all questions and tested on Python 3.
Use Online Code Editor to solve exercise questions.

Table of contents
Exercise 1: Create a function in Python
Exercise 2: Create a function with variable length of arguments
Exercise 3: Return multiple values from a function
Exercise 4: Create a function with a default argument
Exercise 5: Create an inner function
Exercise 6: Create a recursive function
Exercise 7: Assign a different name to function and call it through the new name
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Exercise 9: Find the largest item from list
Exercise 10: Call Function using both positional and keyword arguments
Exercise 11: Create a function with keyword arguments
Exercise 12: Modifies global variable
Exercise 13: Write a recursive function to calculate the factorial
Exercise 14: Create a lambda function that squares a given number
Exercise 15: Use a lambda with the filter() function to get all even numbers from a list
Exercise 16: Use a lambda with the map() function to double each element in a list
Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
Exercise 18: Create Higher-Order Function
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, and prints their values.

Show Hint
Show Solution
# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)
 Run
Exercise 2: Create a function with variable length of arguments
Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.

Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.

Read: variable length of arguments in functions

Function call:

# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
Expected Output:

Printing values
20
40
60

Printing values
80
100
Show Hint
To accept a variable number of positional arguments, allowing functions to take any quantity of these arguments, we use *args as a parameter. (This involves prefixing a parameter name with an asterisk: *).

Using *args, you can pass any number of positional arguments to the function. Internally, all these passed values are collected and represented as a tuple.

Show Solution
Exercise 3: Return multiple values from a function
Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.

Given:

def calculation(a, b):
    # Your Code

res = calculation(40, 10)
print(res)
Expected Output

50, 30
Expected Output:

Show Hint
Show Solution
Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() with the following specifications:

It should accept the employee’s name and salary.
It should display both the name and salary.
If the salary is not provided in the function call, it should default to 9000.
See: Default arguments in function

Given:

showEmployee("Ben", 12000)
showEmployee("Jessa")
Expected output:

Name: Ben salary: 12000
Name: Jessa salary: 9000
"""

def showEmployee(name,  salary = 9000):
    print(f"Name: {name} salary: {salary}")


showEmployee("Ben", 12000)
showEmployee("Jessa")

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise4.py
Name: Ben salary: 12000
Name: Jessa salary: 9000
"""