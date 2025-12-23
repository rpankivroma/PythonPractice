"""
Python math Module — Task

Task Description
Write a Python program that uses the math module to perform several mathematical operations on user-provided numbers.

Requirements

1. Import the math Module
At the top of your script, import math:
import math

2. Ask for a Number
Prompt the user to enter a positive number.
If the number is negative, print:
Please enter a positive number.
and end the program.

3. Square Root and Power
Calculate and print the square root of the number using math.sqrt()
Ask the user for a power (integer)
Raise the number to that power using math.pow() and print the result.

Example:
Enter a positive number: 9
Square root: 3.0
Enter power to raise to: 2
9 raised to 2 is: 81.0

4. Rounding
Print the floor of the number (largest integer ≤ number)
Print the ceil of the number (smallest integer ≥ number)
Use math.floor() and math.ceil()

Example:
Floor: 3
Ceil: 4

5. Absolute Value
Ask the user for another number (can be negative) and print its absolute value using math.fabs().

6. Greatest and Least
Ask the user for two more numbers and then:
Print the maximum using max()
Print the minimum using min()

7. Use a Constant
Print the value of π using math.pi
"""

# Answer

# ------------------------ 1. Import the math Module --------------------------

import math

# --------------------------- 2. Ask for a Number -----------------------------
i=0
while i < 1 :
    user_input = int(input("Please enter a positive number: "))
    if user_input <= 0:
        print("Please enter a positive number")
    else:
        break

# -------------------------- 3. Square Root and Power -------------------------

user_num_input = int(input("Enter a positive number: "))
square_root = math.sqrt(user_num_input)
print("Square root: ", square_root)

user_power_rate = int(input("Enter power to raise to: "))
power_of_rate = math.pow(user_num_input, user_power_rate)
print(f"{user_num_input} raised to {user_power_rate} is: {power_of_rate}")

# --------------------------------- 4. Rounding -------------------------------

print("Floor: ", math.floor(3.5))
print("Ceil: ", math.ceil(3.5))

# ------------------------------- 5. Absolute Value ---------------------------

user_abs_input = int(input("Please enter a number: "))
fabs = abs(user_abs_input)

print("Absolut number: ", fabs)

# --------------------------------- 6. Greatest and Least ---------------------

user_list = list(input("Enter your list: "))
print(user_list)
print("The maximum: ", max(user_list))
print("The minimum: ", min(user_list))

# ------------------------------------ 7. Use a Constant ----------------------

print("The value of π is: ", math.pi)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonMath.py"

Please enter a positive number: 9
Enter a positive number: 9
Square root:  3.0
Enter power to raise to: 2
9 raised to 2 is: 81.0
Floor:  3
Ceil:  4
Please enter a number: -10
Absolut number:  10
Enter your list: 123456789
['1', '2', '3', '4', '5', '6', '7', '8', '9']
The maximum:  9
The minimum:  1
The value of π is:  3.141592653589793
"""