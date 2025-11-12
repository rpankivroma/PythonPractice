"""
Exercise 2: Print the Sum of a Current Number and a Previous number
"""

# Answer:

print("Printing current and previous number sum in a range(10)")

for x in range(0, 10):
    Current_Number = x
    Previous_Number = x - 1
    if Previous_Number == -1:
        Previous_Number = 0 
    print(f"Current Number {Current_Number} Previous Number  {Previous_Number}  Sum:  {Current_Number + Previous_Number}")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_2.py
Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7
Current Number 5 Previous Number  4  Sum:  9
Current Number 6 Previous Number  5  Sum:  11
Current Number 7 Previous Number  6  Sum:  13
Current Number 8 Previous Number  7  Sum:  15
Current Number 9 Previous Number  8  Sum:  17
"""