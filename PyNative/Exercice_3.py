"""
Exercise 3: Print characters present at an even index number
"""
# Answer:

str_ = input("Write a string value: ")
print("Orginal String is: ", str_)
print("Printing only even index chars")

for i in range(len(str_)):
    if (i + 1) % 2 != 0:
        print(str_[i])

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_3.py
Write a string value: PyNative
Orginal String is:  PyNative
Printing only even index chars
P
N
t
v
"""