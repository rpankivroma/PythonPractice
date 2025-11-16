"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
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
