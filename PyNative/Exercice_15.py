"""
Exercise 15: Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected output
Case 1:

base = 2
exponent = 5
2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
Case 2:

base = 5
exponent = 4
5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
"""

def exponent(base, exp):
    res = base ** exp
    print("base:", base)
    print("Exponent:", exp)
    print(f"{base} raises to the power of {exp} is {res}")
    return res
        
exponent(2, 5)
exponent(5, 4)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_15.py
base: 2
Exponent: 5
2 raises to the power of 5 is 32
base: 5
Exponent: 4
5 raises to the power of 4 is 625
"""