"""
Request: Give me one practice task on topic Python veriables thre are a few chepters that should 
be included: Variables, Variable Names, Multiple Variable Values, Output Variable, Global Variable. 
This task should dased on https://www.w3schools.com/python/python_variables.asp

GPT Task: Work with Python Variables
Write a Python program that:

1. Creates valid variables to store your first name, last name, and age.
    - Make sure your variable names follow Python naming rules.
2. Prints your full name in one line using the + operator or f-string.
3. Assigns multiple values in one line to variables x, y, and z 
   (for example: x = "Python", y = "is", z = "fun").
    - Then print them together in a sentence.
4. Create a function called showAge() that:
    - Uses the global keyword to access your age variable.
    - Increases your age by 1 and prints it inside the function.
5. Finally, print the updated value of age outside the function to confirm it changed globally.
"""
# Answer:

firstName = "Roman"
lastName = "Pankiv"
age = 24

print("Full Name:", firstName, lastName)

x, y, z, = "Python", "is", "fine"
print(x, y, z)

def showAge():
    global age 
    age= 25
    print("My new age", age)
showAge()

print("Outside the function, my age is now", age)

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/Part1/PythonVariables.py
Full Name: Roman Pankiv
Python is fine
My new age 25
Outside the function, my age is now 25
"""
