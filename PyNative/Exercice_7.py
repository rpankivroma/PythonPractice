"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:
str_x = "Emma is good developer. Emma is a writer"

Expected Output:
Emma appeared 2 times
"""

# Answer:

str_x = "Emma is good developer. Emma is a writer"
cnt = str_x.count("Emma")
print(f"Emma appeared {cnt}")

"""
Terinal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_7.py
Emma appeared 2
"""