"""
Exercise 16: Check Palindrome Number
A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, 
it reads the same forwards and backward. For example 121, 5005.

Write a code to check if given number is palindrome.
"""

# Answer:

def is_palindrome(number):
    if number < 0:
        return False
    
    original = str(number)
    reversed_number = original[::-1]

    return original == reversed_number

"""user_input = input("Enter a number: ")
num = int(user_input)"""

num = 121

if is_palindrome(num):
        print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")

"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_16.py
Yes. given number is palindrome number

"""