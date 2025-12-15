"""
Exercise 12: Modifies global variable
Define a global variable global_var = 10. Write a function that modifies a global variable value.
"""

# Answer

global_var = 10

def modify_global_var():
    global global_var
    global_var = 20
    print("Inside function:", global_var)

modify_global_var()
print("Outside function:", global_var)

"""
Terminal Output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNativeFunctions/Exercise12.py
Inside function: 20
Outside function: 20
"""