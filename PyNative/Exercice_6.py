"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5

Expected Output:
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
"""

# Answer:

def numbers_divisible_by_5(number_list):
    print("Given list is ", number_list)
    print("Divisible by 5")
    for i in number_list:
        if i % 5 == 0:
            print(i)
    
given_list = [10, 20, 33, 46, 55]
numbers_divisible_by_5(given_list)

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_6.py
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
"""