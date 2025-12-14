"""Exercise 22: Capitalize the first letter of each word in a string
Expected Output:

str1 = "pynative.com is for python lovers"
# Output Pynative.com Is For Python Lovers"""

# Answer:

def CapitalizedSentense(str):
    words = str.split()  
    capitalized_words = [word.capitalize() for word in words] 
    return " ".join(capitalized_words)

str1 = "pynative.com is for python lovers"

CapturasedStr = CapitalizedSentense(str1)
print("Capitalized string:", CapturasedStr)

"""
Terminal Output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_22.py
Capitalized string: Pynative.com Is For Python Lovers
"""