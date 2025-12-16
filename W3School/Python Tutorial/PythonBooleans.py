"""
Request: Give me one practice task on topic Python Booleans, 
based on https://www.w3schools.com/python/python_booleans.asp

GPT Task: Work with Python Booleans
Write a Python program that:
1. Creates two variables:
    - x = 10
    - y = 5
2. Print the results of these comparison expressions using boolean operators:
    - x > y
    - x == y
    - x < y
    - x != y
3. Use an if statement to print:
    - "x is greater than y" if the condition is true
    - Otherwise print "x is not greater than y"
4. Create a variable text = "Python" and check whether "P" is present in it using the in operator.
    -Print True or False based on the result.
5. Use the built-in bool() function to test the truth value of:
    - a non-empty string
    - an empty string
    - the number 0
    - the number 5
Print all their boolean results.
"""

#Answer:

x = 10
y = 5

print(bool(x > y))
print(bool(x == y))
print(bool(x < y))
print(bool(x != y))

if(x > y):
    print("x is greater than y")
else:
    print("x is not greater than y")

text = "Python"
print("P" in text)

print(bool("Hello"))  
print(bool(""))        
print(bool(0))         
print(bool(5))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonBooleans.py
True
False
False
True
x is greater than y
True
True
False
False
True
"""