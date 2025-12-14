"""
Exercise 21: Check if a user-entered string contains any digits using a for loop

Expected Output:

Enter a string: Pynative123Python
The string contains at least one digit.

Enter a string: PYnative
The string does not contain any digits.
"""
# Answer:

def digitsChack(UsersString):
    for i in UsersString:
        if '0' <= i <= '9':
            return True  
    return False 


UsersString = input("Enter a string:")

if digitsChack(UsersString):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_21.py
Enter a string:Pynative123Python
The string contains at least one digit.
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_21.py
Enter a string:PYnative
The string does not contain any digits.
"""