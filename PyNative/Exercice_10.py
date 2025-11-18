"""
Exercise 10: Merge two lists using the following condition
Given two lists of numbers, write Python code to create a new list containing odd numbers from 
the first list and even numbers from the second list.

Given:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:
result list: [25, 35, 40, 60, 90]
"""

# Answer:

def OddNumbers(numbers1, numbers2):
    resList = []

    for i in numbers1:
        if i % 2 == 1:
            resList.append(i)
    
    for x in numbers2:
        if x % 2 == 0:
            resList.append(x)
        
    print("result list:", resList)
    return resList

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

OddNumbers(list1, list2)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_10.py
result list: [25, 35, 40, 60, 90]
"""