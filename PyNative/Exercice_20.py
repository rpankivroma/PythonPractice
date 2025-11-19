"""
Exercise 20: Print Reverse Number Pattern
Expected Output:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
"""

# Answer

for column in range(1, 5 + 1):
    for row in range(5 - column + 1):
        print(column, end=" ")
    print("\t\t")

# Terminal output

# PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
# c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_20.py
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3
# 4 4
# 5