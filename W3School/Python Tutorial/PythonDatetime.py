"""
Python datetime — Task

Task Description
Write a Python program that interacts with the user and 
performs several operations using the datetime module.

Requirements

🕒 1. Display Current Date and Time
Import the datetime module
Print the current date and time in this format:
Today is: 2025-12-22 14:30:15

📅 2. Format the Date
Print:
The current day of the week (e.g., Monday)
The current month name (e.g., December)
Use strftime() to format the output.

Example:
Day of week: Monday
Month: December

⏰ 3. Countdown to a Deadline
Ask the user to enter a future date/time in this format:
YYYY-MM-DD HH:MM

Example input:
Enter deadline (YYYY-MM-DD HH:MM): 2026-01-01 00:00
Calculate how many days, hours, and minutes are left from now until the deadline.
Print:
Time until deadline: 9 days, 5 hours, 12 minutes

🎂 4. Birthday Calculator
Ask the user for their birthday in this format:
YYYY-MM-DD

Calculate:
Their age in years
How many days until their next birthday

Example:
Enter your birthday (YYYY-MM-DD): 2000-07-15
You are 25 years old.
Next birthday in 205 days.

🗓 5. Weekday Checker
Ask the user to input a date:
Enter a date (YYYY-MM-DD): 2026-03-14
Print which day of the week that date falls on.
2026-03-14 is a Saturday.
"""
# Answer 

# ------------------------- Display Current Date and Time ------------------------
import datetime

x = datetime.datetime.now()
print(x.strftime("Today is: %Y-%m-%d %H:%M"))

# ------------------------------ 2. Format the Date ------------------------------

print(x.strftime("Day of week: %A"))
print(x.strftime("Month: %B"))

# -------------------------- 3. Countdown to a Deadline --------------------------

deadline_input = input("Enter deadline (YYYY-MM-DD HH:MM): ")

try:
    deadline = datetime.datetime.strptime(deadline_input, "%Y-%m-%d %H:%M")
    delta = deadline - x

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    if delta.total_seconds() > 0:
        print(f"Time until deadline: {days} days, {hours} hours, {minutes} minutes")
    else:
        print("The deadline has already passed.")

except ValueError:
    print("Invalid date format.")

print("-" * 40)

# ------------------------- 4. Birthday Calculator ---------------------------------

birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

try:
    birthday = datetime.datetime.strptime(birthday_input, "%Y-%m-%d").date()
    today = datetime.date.today()

    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    next_birthday = datetime.date(today.year, birthday.month, birthday.day)
    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)

    days_until_birthday = (next_birthday - today).days

    print(f"You are {age} years old.")
    print(f"Next birthday in {days_until_birthday} days.")

except ValueError:
    print("Invalid birthday format.")

print("-" * 40)

# ----------------------------------- 5. Weekday Checker -----------------------------------

date_input = input("Enter a date (YYYY-MM-DD): ")

try:
    user_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
    print(f"{date_input} is a {user_date.strftime('%A')}.")

except ValueError:
    print("Invalid date format.")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonDatetime.py"

Today is: 2025-12-23 16:05
Day of week: Tuesday
Month: December
Enter deadline (YYYY-MM-DD HH:MM): 2026.01.01 00:00
Invalid date format.
----------------------------------------
Enter your birthday (YYYY-MM-DD): 2001-10-23
You are 24 years old.
Next birthday in 304 days.
----------------------------------------
Enter a date (YYYY-MM-DD): 2001-10-23
2001-10-23 is a Tuesday.
"""