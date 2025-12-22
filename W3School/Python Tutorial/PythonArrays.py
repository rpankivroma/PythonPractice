"""
Python Arrays — Task

Task Description
Create a Python program that manages and analyzes a list of numbers using an array (from the array module) 
and performs several operations on it.

Requirements
1️⃣ Create an Array
Import the Python array module
Create an array named nums containing the following integers:
10, 20, 30, 40, 50]

2️⃣ Add Elements
Ask the user to enter a number
Add this number to the end of the nums array using append()
User input example:
Enter a number to add: 25

3️⃣ Insert an Element
Ask the user for an index and a new number
Insert the number at the given index using the insert() method

User input example:
Enter an index: 2
Enter a number to insert: 15

4️⃣ Remove an Element
Ask the user for a number to remove
Check if the number exists in the array
If it does, remove it using remove()
If it doesn’t, print:
Number not found in the array

5️⃣ Print the Final Array
After all operations, print the final array contents

6️⃣ Compute Stats
Using a loop:
Compute the sum of all numbers in the array
Print the average (rounded or precise)

Expected example:
Sum = 150
Average = 30.0
"""

# Answer
# ------------ Create an Array -------------------------

import array

nums = [10, 20, 30, 40, 50]

# ------------- Add Elements ---------------------------

user_num = nums.append(int(input("Enter a number to add: ")))

# ------------- Insert an Element ----------------------

user_index = int(input("Enter an index: "))
user_insert = int(input("Enter a number to insert: "))
nums.insert(user_index, user_insert)

# -------------- Remove an Element ---------------------

user_RemoveNumber = int(input("Enter the number to remove: "))

if user_RemoveNumber in nums:
    nums.remove(user_RemoveNumber)
else:
    print("Number not found in the array")

# ------------Print the Final Array ---------------------

print(" Final array: ", nums)

# ------------- Compute Stats ---------------------------


sum = 0
for num in nums:
    sum += num

avr = sum / len(nums)

print("Sum = ", sum)
print("Average = ", avr)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonArrays.py"
Enter a number to add: 25
Enter an index: 2
Enter a number to insert: 15
Enter the number to remove: 25
 Final array:  [10, 20, 15, 30, 40, 50]
Sum =  165
Average =  27.5
"""