"""
Request: Give me one practice task on topic Python Data Types 
based on https://www.w3schools.com/python/python_datatypes.asp

GPT Task: Identify and Work with Different Data Types
Write a Python program that:
1. Creates one variable for each of these data types:
    - str → your name
    - int → your age
    - float → your height (in meters)
    - bool → whether you are a student (True or False)
    - list → a list of your three favorite foods
    - tuple → a tuple with three different numbers
    - dict → a dictionary with keys: "country", "city", "language"
2. Prints each variable and its data type using the type() function.
3. Changes one variable’s data type (for example, convert an int to a float) and print the new type.
"""
#Answer:

name = "Roman"
age = 24
height = 1.85
stusentStatus = True
favoriteFoods = ["apple", "bluebary", "rasbery"]
differentNumbers = (1, 2, 3)
generalInfo = {"country" : "Ukraine", "city" : "Lviv", "language" : "Ukrainian"}

print(name, type(name))
print(age, type(age))
print(height,type(height))
print(stusentStatus, type(stusentStatus))
print(favoriteFoods, type(favoriteFoods))
print(differentNumbers, type(differentNumbers))
print(generalInfo, type(generalInfo))

ageInFloat = 24.0
print(ageInFloat, type(ageInFloat))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/Part1/PythonDataTypes.py
Roman <class 'str'>
24 <class 'int'>
1.85 <class 'float'>
True <class 'bool'>
['apple', 'bluebary', 'rasbery'] <class 'list'>
(1, 2, 3) <class 'tuple'>
{'country': 'Ukraine', 'city': 'Lviv', 'language': 'Ukrainian'} <class 'dict'>
24.0 <class 'float'>
"""