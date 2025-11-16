"""
Exercise 5: Check if the first and last numbers of a list are the same

Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.

Given:
numbers_x = [10, 20, 30, 40, 10]
# output True
numbers_y = [75, 65, 35, 75, 30]
# Output False
"""

# Answer:

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("Check X list", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Check Y list", first_last_same(numbers_y))

"""
Terminal oupput:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_5.py
Given list: [10, 20, 30, 40, 10]
Check X list True
Given list: [75, 65, 35, 75, 30]
Check Y list False

"""