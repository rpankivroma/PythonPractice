"""
Requests: Give me one practice task on topic Python Operators including subtopics: 
Python Operators, Arithmetic Operators, Assignment Operators, Comparison Operators, 
Logical Operators, Identity Operators, Membership Operators, Bitwise Operators, 
Operator Precedence. based on https://www.w3schools.com/python/python_operators.asp

GPT Task: Work with Python Operators
Write a Python program that demonstrates each operator type step by step 👇
1. Arithmetic Operators
    Create two variables:
    - a = 10
    - b = 3
    - Use each arithmetic operator and print the result:
    - +, -, *, /, %, **, //
2. Assignment Operators
    Start with:
    - x = 5
    Then use:
    - x += 3
    - x -= 2
    - x *= 4
    - x //= 3
    Print the value of x after each step.
3. Comparison Operators
    Compare a and b using:
    ==, !=, >, <, >=, <=
    and print the boolean results.
4. Logical Operators
    Use:
    - p = True
    - q = False
    Print the results of:
    - p and q
    - p or q
    - not p
5. Identity Operators
    Use:
    - m = ["apple", "banana"]
    - n = ["apple", "banana"]
    - o = m
    Print the results of:
    - m is n
    - m is o 
    - m is not n
6. Membership Operators
    Use:
    - fruits = ["apple", "banana", "cherry"]
    Print:  
    - "banana" in fruits
    - "orange" not in fruits
7. Bitwise Operators
    Use:
    - x = 6   # 110 in binary
    - y = 3   # 011 in binary
    Print results of:
    - x & y
    - x | y
    - x ^ y
    - ~x
    - x << 1
    - x >> 1
8. Operator Precedence
    Print the result of:
    - result = 5 + 2 * 3
    - and explain why it equals that value (order of operations).
"""
#Answer:

# -------------------------------
# 1. Arithmetic Operators
# -------------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) 
print(a ** b)
print(a // b)

# -------------------------------
# 2. Assignment Operators
# -------------------------------

x = 5

print("Assignment Operators:")
x += 3
print(x)
x -= 2
print(x)
x *= 4
print(x)
x //= 3
print(x)

# -------------------------------
# 3. Comparison Operators
# -------------------------------

print("Comparison Operators:")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# -------------------------------
# 4. Logical Operators
# -------------------------------

p = True
q = False

print(" Logical Operators:")
print(p and q)
print(p or q)
print(not q)

# -------------------------------
# 5. Identity Operators
# -------------------------------

m = ["apple", "banana"]
n = ["apple", "banana"]
o = m

print("Identity Operators:")
print(m is n)
print(m is o) 
print(m is not n)

# -------------------------------
# 6. Membership Operators
# -------------------------------

fruits = ["apple", "banana", "cherry"]

print("Membership Operators:")
print("banana" in fruits)
print("orange" not in fruits)

# -------------------------------
# 7. Bitwise Operators
# -------------------------------

x = 6   # 110 in binary
y = 3   # 011 in binary

print("Bitwise Operators:")
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(x >> 1)

# -------------------------------
# 8. Operator Precedence
# -------------------------------

print("Operator Precedence:")

res = 5 + 2 * 3
print(res)
print(f"The result fo this equation is {res}, because operator \"*\" is precedence in  this equation.")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonOperators.py
Arithmetic Operators:
13
7
30
3.3333333333333335
1
1000
3
Assignment Operators:
8
6
24
8
Comparison Operators:
False
True
True
False
True
False
 Logical Operators:
False
True
True
Identity Operators:
False
True
True
Membership Operators:
True
True
Bitwise Operators:
2
7
5
-7
12
3
Operator Precedence:
11
The resut fo this equation is 11, because operator "*" is precedence in  this equation.
"""