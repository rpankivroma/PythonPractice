"""
Exercise 4: Remove first n characters from a string

Write a Python code to remove characters from a string from 0 to n and return a new string.
"""

def remove_chars(word, n):
    # Answer:
    new_word = word[n:] 
    return new_word


print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_4.py
Removing characters from a string
tive
native
"""