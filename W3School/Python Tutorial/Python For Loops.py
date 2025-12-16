"""
🐍 Python For Loops — Task
Task Description
Write a Python program that analyzes a list of numbers using a for loop.

📋 Requirements
Create a list of integers:
numbers = [3, 7, 2, 9, 12, 5, 8, 1]

Use a for loop to iterate through the list.

During the loop:

If a number is even, print:
Even number found: X

If a number is odd, print:
Odd number found: X

Use continue to skip printing numbers that are less than 3.

Use break to stop the loop if the number 12 is found, and print:
Stopping the loop at 12

Count how many numbers were checked before the loop stopped.

Use a for … else block:

If the loop finishes without encountering 12, print:
Loop completed without finding 12

After the loop ends, print the total count of checked numbers.

🧠 Example Output
Odd number found: 3
Odd number found: 7
Even number found: 2
Odd number found: 9
Stopping the loop at 12
Numbers checked: 5
"""

# Answer 

numbers = [3, 7, 2, 9, 12, 5, 8, 1]
checked_count = 0

for i in numbers:
    if i < 3:
        continue

    checked_count += 1

    if i == 12:
        print("Stopping the loop at 12")
        break

    if i % 2 == 0:
        print("Even number found: ", i)
    else:
        print("Odd number found: ", i)    
    
else:
    print("Loop completed without finding 12")

print(f"Numbers checked: ", checked_count)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/Python For Loops.py"
Odd number found:  3
Odd number found:  7
Odd number found:  9
Stopping the loop at 12
Numbers checked:  4
"""