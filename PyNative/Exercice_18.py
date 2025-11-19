"""
Exercise 18: Check if a given year is a leap year
A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. 
This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.

Write a code find if a given year is a leap year.

Given:

year1 = 2020 
# Output True

year2 = 2025
# Output False
"""

# Answer

def CheckOnLeapYear(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 1:
        return False
    else:
        return False
    
year1 = 2020 
year2 = 2025

print(CheckOnLeapYear(year1))
print(CheckOnLeapYear(year2))

"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_18.py

True
False
"""