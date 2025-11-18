"""
Exercise 14: Print a downward half-pyramid pattern of stars
* * * * *  
* * * *  
* * *  
* *  
*
"""

# Answer:

for column in range(6, 0, -1):
    for row in range(0, column - 1):
        print("*", end=" ")
    print("\t\t")

"""
Terminal output 
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_14.py
* * * * * 
* * * * 
* * *
* *
*
"""