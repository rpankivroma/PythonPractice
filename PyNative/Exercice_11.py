"""
Exercise 11: Get each digit from a number in the reverse order.
For example, If the given integer number is 7536, the output shall be “6 3 5 7“, 
with a space separating the digits.

Given:
number = 7536
# Output 6 3 5 7
"""

def revOrder(num):
    
    resList = []

    for i in str(num):
        resList.append(i)

    resList.reverse()
    print("Output", resList)
    return resList

number = 7536
revOrder(number)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_11.py
Output ['6', '3', '5', '7']
"""