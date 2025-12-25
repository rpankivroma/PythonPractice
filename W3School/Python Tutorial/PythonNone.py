"""
Python None Task: User Profile Checker

📌 Goal
Write a Python program that works with missing values using None.

🧾 Given Data
username = "alex"
email = None
age = None
country = "Ukraine"

📝 Tasks

Task 1 — Check for missing values
Check which variables contain None and print a message like:
Email is missing
Age is missing
(Do not use == None)

Task 2 — Function returning None
Create a function get_user_age() that:
returns the age if it exists
returns None if the age is missing
Print the returned value.
Task 3 — Using is and is not
Use is / is not to check:
if the user has provided an email
if the user has provided an age

Task 4 — Default values
If age is None, print:
Age not provided
Otherwise print:
User is 25 years old

Task 5 — None vs False
Create a variable:
is_active = None
Check and print:
whether the user is active
whether the activity status is unknown

Task 6 — Function with optional return
Write a function print_country() that:
prints the country if it exists
returns None
Print the return value and explain what it is.

🎯 Requirements
Use None
Use is / is not
Show a function that returns None
Do not compare None using ==
"""

# Answer

username = "alex"
email = None
age = None
country = "Ukraine"

# -------------------------------- Task 1 — Check for missing values ---------------------------------

def none_checker(**kwrd):
    for name, value in kwrd.items():
        if value is None:
            print (name, " is missing")

none_checker(username=username, email=email, age=age, country=country)

# --------------------------------- Task 2 — Function returning None ----------------------------------

def get_user_age(age):
    if age is not None:
        return age
    else:
        return None
    
print(get_user_age(age))

# ------------------------------------ Task 4 — Default values -----------------------------------------

if age is None:
    print("Age not provided")
else:
    print("User is 25 years old")

# ------------------------------------ Task 5 — None vs False -------------------------------------------

is_active = None

if is_active is True:
    print("The user is active")
elif is_active is False:
    print("The user isn't active")
elif is_active is None:
    print("The activity status is unknown")

# ----------------------------- Task 6 — Function with optional return ----------------------------------

def print_country(country):
    if country is None:
        return None
    else:
        return country
    
print(print_country(country))

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonNone.py"
email  is missing
age  is missing
None
Age not provided
The activity status is unknown
Ukraine
"""