"""
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

Expected Output:
For example, suppose the income is 45000, and the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000
"""

# Answer

def TaxCalculator(income):
    tax = 0
    
    if income > 10000:
        income -= 10000
    else:
        return 0 

    if income > 10000:
        tax += 10000 * 0.10
        income -= 10000
    else:
        tax += income * 0.10
        return tax

    tax += income * 0.20

    return tax

number = 45000
print("Tax: $" + str(TaxCalculator(number)))
"""
Terminal output
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
c:/Users/trade/Desktop/PythonPractice/PythonPractice/PyNative/Exercice_12.py
Tax: $6000.0
"""