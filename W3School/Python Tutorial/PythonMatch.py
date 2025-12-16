"""
Request: Give me one practice task on topic The Python Match Statement
based on: https://www.w3schools.com/python/python_match.asp

GPT Task: Use match…case to classify items
You are working on a simple shopping cart scenario.
Write a Python program that:
1. Creates a variable product which can take one of the following string values:
    - "apple", "banana", "milk", "bread", "wine", or something else.
2. Use a match statement to print the type of the product category:
    - For "apple" or "banana": print "Fruit".
    - For "milk" or "bread": print "Grocery".
    - For "wine": print "Alcohol".
    - For any other product: print "Other item" (use the default case _).
3. Then, extend your match with guards (an if condition in a case) using a second variable price.
    - If product is "wine" and price >= 20: print "Premium Alcohol".
    - Otherwise if product is "wine" and price < 20: print "Standard Alcohol".
    - You can keep the earlier category printing as well.
4. Combine multiple values with the pipe | operator for simpler cases (for example "apple" | "banana").
5. Try the program with several combinations of product and price to confirm all branches work.
"""
# Answer:
import random

#----------------------------------------------------------------------
# 1. Creates a variable
#----------------------------------------------------------------------

products = ["apple", "banana", "milk", "bread", "wine"]
product = random.choice(products)
price = random.randint(1, 40)

#----------------------------------------------------------------------
# 2. Use a match statement to print the type of the product category
# 3. Extend the match with guards (an if condition in a case) using 
#    a second variable price.
#----------------------------------------------------------------------

match product:
    case "apple" | "banana":
        print(f"Your chose a {product}. It is Fruit")
    case "milk" | "bread":
        print(f"Your chose a {product}. It is Grocery")
    case "wine":
        print(f"Your chose a {product}. It is Alcohol") 
        if price >= 20:
            print(f"Premium Alcohol. Its price {price}")
        else:
            print(f"Standard Alcohol. Its price {price}")
    case _:
        print(f"Your chose a {product}. It is Other item")

"""
Terminal outputs:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonMatch.py
Your chose a milk. It is Grocery
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonMatch.py
Your chose a wine. It is Alcohol
Standard Alcohol. Its price 16
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonMatch.py
Your chose a wine. It is Alcohol
Standard Alcohol. Its price 18
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonMatch.py
Your chose a apple. It is Fruit
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonMatch.py
Your chose a wine. It is Alcohol
Premium Alcohol. Its price 30
"""