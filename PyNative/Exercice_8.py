"""
Exercise 8: Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

# Answer:

for x in range(6):
    for i in range(x):
        print (x, end=" ") 
    print("\n")

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_8.py

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5
"""