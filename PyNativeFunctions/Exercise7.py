"""
Exercise 7: Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.

Given:

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
You should be able to call the same function using

show_student(name, age)
"""

# Answer

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)


show_student = display_student 

show_student("Emma", 26)


"""
Trminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise7.py
Emma 26
Emma 26
"""