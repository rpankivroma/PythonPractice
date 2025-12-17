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

# -------- Task A — Basic Function & Arguments --------

def GreatingFunc(name, age):
    return f"Hello {name}! You are {age} years old."

# print(GreatingFunc("Roman", 24))

# --------------- Task B — Using *args ----------------
import math

def sum_all(*args):
    result = sum(args)
    print("sum_all", args)
    print("The sum is: ", result)
    
"""sum_all(2,5,3)
sum_all(2,5)"""

