"""
Request: Give me one practice task on topic Python If...Else Statement including subtopics in one task: 
    - Python If 
    - Python Elif 
    - Python Else 
    - Shorthand If Logical Operators 
    - Nested If 
    - Pass Statement 
    based on: https://www.w3schools.com/python/python_conditions.asp

GPT Practice Task: Python If...Else Statements
You are creating a small grading program for students based on their exam score and attendance.
Follow the steps below using if, elif, else, and logical operators.
Task Instructions
1. Create two variables:
    score = 85
    attendance = 90
2. Python If
    - If score is greater than or equal to 90, print "Excellent!".
3. Python Elif
    - If score is between 80 and 89, print "Very Good".
    - If score is between 70 and 79, print "Good".
    - Otherwise, print "Needs Improvement".
4. Python Else
    - Use an else statement to catch all scores below 70 and print "Failed".
5. Shorthand If
    - Write a one-line if statement that prints "Perfect score!" if score == 100.
6. Logical Operators
    - If score >= 80 and attendance >= 85, print "Eligible for certificate".
    - If score >= 80 or attendance >= 85, print "Good effort".
7. Nested If
    - If score >= 80:
    - Inside it, check if attendance >= 90.
    - If true, print "Outstanding performance!".
8. Pass Statement
    - Create a placeholder condition that checks if score < 0 and use the pass statement (to show how it works).
"""

# Answer:

# -------------------------------------------------
# 1. Create two variables
# -------------------------------------------------

score = 85
attendance = 90

# -------------------------------------------------
# 2. Python If
# -------------------------------------------------

if score >= attendance:
    print("Excellent!")

# -------------------------------------------------
# 3. Python Elif
# -------------------------------------------------

if 80 <= score <= 89:
    print("Very Good")
elif 70 <= score <= 79:
    print("Good")
elif score < 79:
    print("Needs Improvement")

# -------------------------------------------------
# 4. Python Else
# -------------------------------------------------

else:
    print("Failed")

# -------------------------------------------------
# 5. Shorthand If
# -------------------------------------------------

if score == 100: print("Perfect score!") 

# -------------------------------------------------
# 6. Logical Operators
# -------------------------------------------------

if score >= 80 and attendance >= 85: print("Eligible for certificate")
if score >= 80 or attendance >= 85: print("Good effort")

# -------------------------------------------------
# 7. Nested If
# -------------------------------------------------

if score >= 80:
    if attendance >= 90:
        print("Outstanding performance!")

# -------------------------------------------------
# 8. Nested If
# -------------------------------------------------

if score < 0:
    pass

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/PythonIfStatement.py
Very Good
Eligible for certificate
Good effort
Outstanding performance!
"""