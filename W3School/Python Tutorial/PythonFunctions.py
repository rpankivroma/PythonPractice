"""
Python Functions — Multi-Part Task
You will build a small utility module called math_utils.py that performs several operations using functions and the Python features listed below.

✅ Task A — Basic Function & Arguments
Write a function greet(name, age) that:
Takes two parameters: name (string) and age (int)
Returns a greeting like:
"Hello Alex! You are 25 years old."

✅ Task B — Using *args
Write a function sum_all(*args) that:
Takes a flexible number of numeric arguments
Returns the total sum
Example:
>>> sum_all(3, 5, 7)
15

✅ Task C — Using **kwargs
Write a function describe_person(**kwargs) that:
Accepts any named info about a person
Prints each key and value
Example:describe_person(name="Sam", hobby="chess", country="Japan")
Output:
name : Sam
hobby : chess
country : Japan

✅ Task D — Scope
Define a global variable counter = 0
Write a function increase() that:
Increases counter by 1
Returns the new value
Demonstrate scope by printing the value before and after calling increase()

✅ Task E — Decorators
Write a decorator debug(func) that:
Prints function name and arguments before calling
Prints result after calling
Apply @debug to a function multiply(a, b) to test it
Expected output example:
Calling: multiply(3,5)
Result: 15

✅ Task F — Lambda Functions
Create a lambda that squares a number:
square = lambda x: x * x
Use it to print the square of 8

✅ Task G — Recursion
Write a function factorial(n) that:
Uses recursion to return n!
Handles n == 0 (base case)
Example:
factorial(5)  # 120
"""

# Answer

print ("-------- Task A — Basic Function & Arguments ---------------")

def GreatingFunc(name, age):
    return f"Hello {name}! You are {age} years old."

print(GreatingFunc("Roman", 24))

print("--------------- Task B — Using *args -----------------------")
import math

def sum_all(*args):
    result = sum(args)
    print("sum_all", args)
    print("The sum is: ", result)
    
sum_all(2,5,3)
sum_all(2,5)

print("---------------- Task C — Using **kwargs -------------------")

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

describe_person(name="Sam", hobby="chess", country="Japan")

print("------------------- Task D — Scope -------------------------")

global counter
counter = 0
print(counter)

def increase():
    counter = 1
    print(counter)
    return counter

increase()

print("----------------- Task E — Decorators -----------------------")

def debug(func):
    def wrapper(*args):
        print(f"Calling: {func.__name__}{args}")
        return func(*args)
    return wrapper


@debug
def multiply(a, b):
    result = a * b
    print(f"Result: {result}")
    return result

multiply(3, 5)

print("---------------- Task F — Lambda Functions -------------------")

square = lambda x: x * x

print("The square of 8 is", square(8))

print("------------------Task G — Recursion -------------------------")

def factorial(n):
    if n == 0 or n == 1:   
        return 1
    return n * factorial(n - 1)

print(factorial(5))

"""
Terminal output: 
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonFunctions.py"

-------- Task A — Basic Function & Arguments ---------------
Hello Roman! You are 24 years old.
--------------- Task B — Using *args -----------------------
sum_all (2, 5, 3)
The sum is:  10
sum_all (2, 5)
The sum is:  7
---------------- Task C — Using **kwargs -------------------
name : Sam
hobby : chess
country : Japan
------------------- Task D — Scope -------------------------
0
1
----------------- Task E — Decorators -----------------------
Calling: multiply(3, 5)
Result: 15
---------------- Task F — Lambda Functions -------------------
The square of 8 is 64
------------------Task G — Recursion -------------------------
120
"""