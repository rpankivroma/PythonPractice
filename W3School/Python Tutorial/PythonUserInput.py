"""
Python User Input Task: Simple Banking Console App

📌 Goal
Create a console program that interacts with the user using input() and performs basic calculations.

🧾 Program Requirements
Your program should ask the user for information and then print a summary.

📝 Tasks

Task 1 — Get user name
Ask the user to enter their name and print:
Hello, Alice!

Task 2 — Get user age
Ask the user for their age.
Convert the input to an integer
Print how old the user will be next year
Example:
Next year you will be 26 years old.

Task 3 — Get bank balance
Ask the user to enter their bank balance.
Convert the input to a float
Print the balance formatted to 2 decimal places
Example:
Your current balance is $1234.50

Task 4 — Deposit amount
Ask how much money the user wants to deposit.
Add it to the balance
Print the new balance

Task 5 — Simple validation
If the user enters a negative deposit, print:
Invalid deposit amount
Otherwise:
Deposit successful!

Task 6 — Final summary
Print a final formatted summary:

----- ACCOUNT SUMMARY -----
Name: Alice
Age next year: 26
Final balance: $1450.75
---------------------------

🎯 Requirements
Use input()
Use int() and float()
Use basic if statements
No external libraries
No advanced error handling (try/except not required)
"""

# Answer

# --------------------------------------- Task 1 — Get user name ---------------------------------------

i = 0
while i < 5:
    users_name = str(input("Enter your name: "))
    if users_name.isdigit():
        print("Please enter yur name using abc.")
        i += 1
    else:
        print(f"Hello, {users_name}!")
        break

# ---------------------------------------  Task 2 — Get user age ---------------------------------------

i = 0
while i < 5:
    try:
        users_age = int(input("Enter your age: "))
        print(f"Next year you will be {users_age + 1} years old.")
        break
    except ValueError:
        print("Please enter a number of your age.")
        i += 1

# ---------------------------- Task 4 — Deposit amount / Task 5 — Simple validation --------------------

i = 0
while i < 5:
    try:
        users_balance = float(input("Enter your balance: "))
        print(f"our current balance is ${users_balance}")
        if users_balance < 0:
            print("Invalid deposit amount")
        else:
            print("Deposit successful!")
            break
    except ValueError:
        print("Please enter a number of your balance.")
        i += 1

# ------------------------------------- Task 6 — Final summary -----------------------------------------

final_amount_summary = f"""
----- ACCOUNT SUMMARY -----
Name: {users_name}
Age next year: {users_age + 1}
Final balance: ${users_balance}
---------------------------
"""
print(final_amount_summary)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonUserInput.py"
Enter your name: Roman
Hello, Roman!
Enter your age: 24
Next year you will be 25 years old.
Enter your balance: 13500
our current balance is $13500.0
Deposit successful!

----- ACCOUNT SUMMARY -----
Name: Roman
Age next year: 25
Final balance: $13500.0
---------------------------
"""